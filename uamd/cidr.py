#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author:        alisue
# date:            2011/03/22
#
u"""
.. data:: default_loader
    the :class:`DefaultLoader` instance. use this instance insted of
    creating new instance with your self. the loader save cache in instance
    that's why you should not create the loader instance your self.
"""
from IPy import IP
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from dateutils import relativedelta

class CIDR(object):
    u"""
    Classless Inter-Domain Routing class. 
    """
    def __init__(self, data=[]):
        u"""Constructor of CIDR class

        :params list data:   list of IP in CIDR
        """
        self._data = [IP(x) for x in data]
    
    def __iter__(self):
        return self._data.__iter__()
    
    def __contains__(self, x):
        u"""whether the cidr contain the IP"""
        for addr in self._data:
            if x in addr: return True
        return False
    
    def __unicode__(self):
        return self._data

class Loader(object):
    u"""CIDR loader base class. subclass must override :meth:`get` method."""
    def get(self, carrier):
        u"""get cidr via carrier. subclass must override this method.
        
        :param string carrier:  the carrier name of CIDR you want.
        :rtype:                 :class:`CIDR` instance
        """
        raise NotImplementedError
    
    def fetch(self, carrier):
        u"""fetch CIDR via carrier from Internet.
        
        :param string carrier:  the carrier name of CIDR you want. ``'docomo'``, 
                                ``'kddi'`` and ``'softbank'`` is supported.
        :rtype:                 :class:`CIDR` instance
        """
        carrier = carrier.lower()
        if carrier == 'docomo':
            return self._fetch_docomo()
        elif carrier == 'kddi':
            return self._fetch_kddi()
        elif carrier == 'softbank':
            return self._fetch_softbank()
    def _fetch_docomo(self):
        url = r"http://www.nttdocomo.co.jp/service/imode/make/content/ip/"
        soup = BeautifulSoup(urlopen(url).read())
        data = [li.string for li in soup.find("ul", "normal txt")("li")]
        return CIDR(data)
    def _fetch_kddi(self):
        url = r"http://www.au.kddi.com/ezfactory/tec/spec/ezsava_ip.html"
        soup = BeautifulSoup(urlopen(url).read())
        soup = soup.find("table")("table")[16]("td", nowrap=None, bgcolor=None)
        data = []
        for i in xrange(0, len(soup), 2):
            addr = soup[i].find("div", "TableText").string
            mask = soup[i+1].find("div", "TableText").string
            data.append(addr+mask)
        return CIDR(data)
    def _fetch_softbank(self):
        url = r"http://creation.mb.softbank.jp/web/web_ip.html"
        soup = BeautifulSoup(urlopen(url).read())
        soup = soup.find("div", id="main").find("div", "contents")
        soup = soup.find("table")("tr")[1].find("table")
        soup = soup.find("table")("tr")[6]("td", bgcolor="#eeeeee")
        data = [x.string.replace('&nbsp;', '') for x in soup]
        return CIDR(data)
    
class DefaultLoader(Loader):
    u"""Default cidr loader
    
    this loader store fetched cidr to instance and return it if not expired (default: 1 week)
    so if you can keep the instance, using this loader is good choice.
    if you are interested in DatabasedLoader. See https://github.com/alisue/django-mfw/blob/master/mfw/core/cidr.py
    for more detail (the django's database model based loader)

    .. attribute:: EXPIRE
        the expire :class:`dateutils.relativedelta` instance. the default is set as one week.
    """
    
    EXPIRE = relativedelta(weeks=1)
    
    def _get_cache(self, carrier):
        name = '_%s_cache' % carrier.lower()
        cidr, expire = getattr(self, name, (None, None))
        if expire and datetime.now() < expire:
            return cidr
        return None
    def _set_cache(self, carrier, cidr):
        name = '_%s_cache' % carrier.lower()
        expire = datetime.now() + self.EXPIRE
        setattr(self, name, (cidr, expire))
    
    def get(self, carrier):
        u"""get cidr via carrier from instance cache or internet
        
        :param string carrier:  the carrier name of CIDR you want.
        :rtype:                 :class:`CIDR` instance
        """
        cidr = self._get_cache(carrier)
        if cidr is None:
            cidr = self.fetch(carrier)
            self._set_cache(carrier, cidr)
        return cidr
default_loader = DefaultLoader()

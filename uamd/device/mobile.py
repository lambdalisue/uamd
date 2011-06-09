#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
from . import Device
import re

class Mobile(Device):
    u"""
    The base class of mobile device
    """
    _carrier = None
    _encoding = None
    
    def __init__(self, name=None, support_cookie=None, uid=None):
        u"""Constructor of the class

        :param string name:         the name of device. it is also stored in ``model`` property
        :param bool support_cookie: whether the device support cookie
        :param string uid:          the carrier's UID
        """
        super(Mobile, self).__init__(name, support_cookie)
        self._uid = uid
        self._model = name
        
    def __unicode__(self):
        return u"%s %s" % (self.carrier, self.name)
    
    # Properties
    carrier = property(lambda self: self._carrier)
    encoding = property(lambda self: self._encoding)
    uid = property(lambda self: self._uid)
    model = property(lambda self: self._model)
    
#
# NTT DoCoMo
#------------------------------------------
class DoCoMo(Mobile):
    _carrier = u'docomo'
    _encoding = u'cp932'
    _pattern = re.compile(r"DoCoMo/(?P<type>[12].0)[ \/]")
    _pattern_mova = re.compile(r"DoCoMo/1.0/(?P<name>[^/]*)(?:/c(?P<cache>\d*)|)")
    _pattern_foma = re.compile(r"DoCoMo/2.0 (?P<name>[^\(]*)\(c(?P<cache>\d*)")
    
    def __init__(self, type, name=None, support_cookie=None, uid=None):
        super(DoCoMo, self).__init__(name, support_cookie, uid)
        self._type = type
    
    # Properties
    type = property(lambda self: self._type)
    
    # Class method
    def _parse_mova(cls, ua):
        m = cls._pattern_mova.match(ua)
        name, cache = m.groups()
        cache = int(cache) if cache else 5
        return name, cache
    _parse_mova = classmethod(_parse_mova)
    def _parse_foma(cls, ua):
        m = cls._pattern_foma.match(ua)
        name, cache = m.groups()
        cache = int(cache)
        return name, cache
    _parse_foma = classmethod(_parse_foma)
    def factory(cls, meta):
        uid = meta.get('HTTP_X_DCMGUID', None)
        ua = meta.get('HTTP_USER_AGENT', None)
        if cls._pattern_mova.match(ua):
            name, cache = cls._parse_mova(ua)
            type = u"MOVA"
        elif cls._pattern_foma.match(ua):
            name, cache = cls._parse_foma(ua)
            type = u"FOMA"
        else:
            raise NotImplementedError(u"unknown user agent for DoCoMo (%s)" % ua)
        support_cookie = cache >= 500
        return cls(type, name, support_cookie, uid)
    factory = classmethod(factory)
    
class KDDI(Mobile):
    _carrier = u'kddi'
    _encoding = u'cp932'
    _pattern = re.compile(r"(?:(?:KDDI-)|(?:SIE-))(?P<name>[^\s/]*)")
    
    def __init__(self, hdml, name=None, support_cookie=None, uid=None):
        super(KDDI, self).__init__(name, support_cookie, uid)
        self._hdml = hdml
    
    # Properties
    hdml = property(lambda self: self._hdml)
    
    # Class method
    def factory(cls, meta):
        uid = meta.get('HTTP_X_UP_SUBNO', None)
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        name = m.group('name')
        support_cookie = True
        hdml = ua.startswith('SIE')
        return cls(hdml, name, support_cookie, uid)
    factory = classmethod(factory)
    
class SoftBank(Mobile):
    _carrier = u'softbank'
    _encoding = u'utf8'
    _pattern = re.compile(r"(?P<type>J-PHONE|Vodafone|SoftBank)/(?P<version>[\d\.]*)/(?P<name>[^/\[]*)")
    
    def __init__(self, type, name=None, support_cookie=None, uid=None):
        super(SoftBank, self).__init__(name, support_cookie, uid)
        self._type = type
    
    # Properties
    type = property(lambda self: self._type)
    
    # Class method
    def factory(cls, meta):
        uid = meta.get('HTTP_X_JPHONE_UID', None)
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        type, version, name = m.groups()
        if type == 'J-PHONE':
            support_cookie = version.startswith('5')
        else:
            support_cookie = True
        return cls(type, name, support_cookie, uid)
    factory = classmethod(factory)

devices = (DoCoMo, KDDI, SoftBank)

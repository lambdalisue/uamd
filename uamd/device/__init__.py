#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
class Device(object):
    _name = None
    _support_cookie = None
    _pattern = None
    
    def __init__(self, name=None, support_cookie=None):
        self._name = name if name is not None else self._name
        self._support_cookie = support_cookie if support_cookie is not None else self._support_cookie
        
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__().encode("utf8")
    def __getattr__(self, name):
        return None
    
    # Properties
    name = property(lambda self: self._name)
    support_cookie = property(lambda self: self._support_cookie)
    
    # Class method
    def fastcheck(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        return cls._pattern.match(ua) if ua else False
    fastcheck = classmethod(fastcheck)

class DummyDevice(Device):
    _name = u"Unknown device"
    _support_cookie = True
    
import browser
import mobile
import smartphone

devices = tuple(list(browser.devices) \
    + list(mobile.devices) \
    + list(smartphone.devices))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
from . import Device
from mobile import SoftBank
import re

class SmartPhone(Device):
    _support_flush = None
    def __init__(self, name=None, support_cookie=None, support_flush=None):
        super(SmartPhone, self).__init__(name, support_cookie)
        self._support_flush = support_flush if support_flush is not None else self._support_flush 
    # Properties
    support_flush = property(lambda self: self._support_flush)
    is_smartphone = property(lambda self: True)

#
# Apple family
#---------------------------------
class iPhone(SmartPhone):
    _name = u"iPhone"
    _support_cookie = True
    _support_flush = False
    _pattern = re.compile(r"Mozilla/[\d\.]* \(iPhone; U; CPU (?:(?:iPhone OS (?P<version>[\w_]*))|)")
    _carrier = SoftBank._carrier
    _encoding = u"utf8"
    
    def __init__(self, version):
        super(iPhone, self).__init__()
        self._version = version
        
    def __unicode__(self):
        return u"%s %s" % (self.name, self.version)
    
    # Properties
    version = property(lambda self: self._version)
    carrier = property(lambda self: self._carrier)
    encoding = property(lambda self: self._encoding)
    
    # Class method
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        version = m.group('version') or '1_0'
        version = version.replace('_', '.')
        return cls(version)
    factory = classmethod(factory)
    
class iPodTouch(iPhone):
    _name = u"iPod Touch"
    _pattern = re.compile(r"Mozilla/[\d\.]* \(iPod; U; CPU (?:(?:iPhone OS (?P<version>[\w_]*))|)")
    _carrier = None
class iPad(iPhone):
    _name = u"iPad"
    _pattern = re.compile(r"Mozilla/[\d\.]*\(iPad; U; CPU (?:(?:iPhone OS (?P<version>[\w_]*))|)")

#
# Google Android family
#--------------------------------------------
class Android(SmartPhone):
    _name = u"Android"
    _support_cookie = True
    _support_flush = True
    _pattern = re.compile(r"Mozilla/[\d\.]* \(Linux; U; Android (?P<version>[^;]*);(?P<language>[^;]*);(?P<model>[^;\)]*)")
    
    def __init__(self, version, model):
        super(Android, self).__init__()
        self._version = version
        self._model = model
    
    def __unicode__(self):
        return u"%s %s (%s)" % (self.name, self.version, self.model)
    
    # Properties
    version = property(lambda self: self._version)
    model = property(lambda self: self._model)
    
    # Class method
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        version = m.group('version')
        language = m.group('language')
        model = m.group('model')
        return cls(version, model)
    factory = classmethod(factory)

devices = (iPhone, iPodTouch, iPad, Android)
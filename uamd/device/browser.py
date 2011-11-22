#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:    alisue
# Date:        2011/03/24
#
from . import Device
import re

class Browser(Device):
    _support_cookie = True
    def __init__(self, version, os, name=None, support_cookie=None):
        super(Browser, self).__init__(name, support_cookie)
        self._version = version
        self._os = os
        
    # Properties
    version = property(lambda self: self._version)
    os = property(lambda self: self._os)
    
class InternetExplorer(Browser):
    _name = u"Internet Explorer"
    _pattern = re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE (?P<version>[\d\.]*); (?P<os>[^;]*);")
    
    # Class method
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        version, os = m.groups()
        return cls(version, os)
    factory = classmethod(factory)

class GoogleChrome(Browser):
    _name = u"Google Chrome"
    _pattern = re.compile(r"Mozilla/[\d\.]* \([^;]*; U; (?P<os>[^;]*); .*Chrome/(?P<version>[\d\.]*)")
    
    # Class method[^\)]*\) AppleWebKit/[\d\.]* (KHTML, like Gecko)
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        os, version = m.groups()
        return cls(version, os)
    factory = classmethod(factory)

class Lunascape(Browser):
    _name = u"Lunascape"
    _pattern = re.compile(r"Mozilla/[\d\.]* \(compatible; MSIE [\d\.]*; (?P<os>[^;]*); .*Lunascape (?P<version>[^\)]*)\)")
    
    # Class method
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        os, version = m.groups()
        return cls(version, os)
    factory = classmethod(factory)

class Firefox(Browser):
    _name = u"Firefox"
    _pattern = re.compile(r"Mozilla/[\d\.]* \([^;]*; U; (?P<os>[^;]*); .*Firefox/(?P<version>[\d\.]*)")
    
    # Class method
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        os, version = m.groups()
        return cls(version, os)
    factory = classmethod(factory)
    
class Safari(Browser):
    _name = u"Firefox"
    _pattern = re.compile(r"Mozilla/[\d\.]* \([^;]*; U; (?P<os>[^;]*); .*Version/(?P<version>[\d\.]*) Safari")
    
    # Class method
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        m = cls._pattern.match(ua)
        os, version = m.groups()
        return cls(version, os)
    factory = classmethod(factory)
    
class Opera(Browser):
    _name = u"Opera"
    _pattern = None
    _pattern_s = re.compile(r"Opera/(?P<version>[\d\.]*) \((?P<os>[^;]*);")
    _pattern_l = re.compile(r"Mozilla/[\d\.]* \([^;]*; [^;]*; (?P<os>[^;]*); .*Opera (?P<version>[\d\.]*)")
    
    # Class method
    def fastcheck(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        return 'Opera' in ua if ua else False
    
    fastcheck = classmethod(fastcheck)
    def factory(cls, meta):
        ua = meta.get('HTTP_USER_AGENT', None)
        if cls._pattern_s.match(ua):
            m = cls._pattern_s.match(ua)
            version, os = m.groups()
        elif cls._pattern_l.match(ua):
            m = cls._pattern_l.match(ua)
            os, version = m.groups()
        else:
            raise NotImplementedError(u"unknown Opera user agent (%s)" % ua)
        return cls(version, os)
    factory = classmethod(factory)

devices = (Firefox, GoogleChrome, Lunascape, Safari, Opera, InternetExplorer)

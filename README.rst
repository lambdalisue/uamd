``uamd`` (User Agent Mobile Detect) is for detecting japanese mobile phone
from HTTP_USER_AGENT and return device information include UID from HTTP Header
and spoof check by CIDR of each carrier


Install
=================================================
::
    
    sudo pip install uamd

or::

	sudo pip install git+git://github.com/lambdalisue/uamd.git#egg=uamd


Required (Automatically installed)
=================================================
+ IPy
+ BeautifulSoup


How to use
=================================================
::

	>>> META = {
	>>> 	'HTTP_USER_AGENT': u"J-PHONE/2.0/J-SH02",
	>>> 	'HTTP_X_JPHONE_UID': u"XXXXXXX",
	>>> 	'REMOTE_ADDR': u"123.108.237.0",			# Valid IP for Softbank (2011/03/22)
	>>> }
	>>> deice = uamd.detect(META)
	>>> device.name
	u'J-SH02'
	>>> device.type
	u'J-Phone'
	>>> device.uid
	u'XXXXXXX'
	>>> device.spoof
	False

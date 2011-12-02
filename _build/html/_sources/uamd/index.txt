##############################################
uamd API Reference
##############################################
Device detection library via HTTP_USER_AGENT

Introduction
==============================================
**uamd** is library for detecting device via HTTP_USER_AGENT.

Currently this library can detect the device listed below

+ DoCoMo mobile phone
+ KDDI mobile phone
+ SoftBank mobile phone  
+ iPhone/iPod Touch/iPad
+ Android
+ Internet Explorer
+ Google Chrome
+ Firefox
+ Opera
+ Lunascape

The device doesn't listed above will treat as :class:`device.DummyDevice`
which will treated as device which support cookie and has no carrier (treated like as PC Browser)

Methods
==============================================

.. automodule:: uamd
   :members: 

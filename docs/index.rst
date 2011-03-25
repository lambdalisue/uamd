.. uamd documentation master file, created by
   sphinx-quickstart on Sat Mar 26 01:58:36 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##############################################
Welcome to uamd
##############################################
**uamd** is a library for detecting device via HTTP_USER_AGENT.
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

Getting started
=============================================
If you are new to uamd, you may want to start with these documents to get you up and running

.. toctree::
    :maxdepth: 2
    :glob:

    tutorial/index
    tutorial/device

Table of contents
=============================================
.. toctree::
    :maxdepth: 2
    :glob:

    uamd/*

Indices and tables
============================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


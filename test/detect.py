#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author:        alisue
# date:            2011/03/22
#
import unittest

import uamd

class TestCase(unittest.TestCase):

    # DoCoMo
    #---------------------------------------
    def test_docomo_mova(self):
        META = {
            'HTTP_USER_AGENT': u"DoCoMo/1.0/D502i",
            'HTTP_X_DCMGUID': u"XXXXXXX",
            'REMOTE_ADDR': u"210.153.84.0",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"D502i")
        self.assertEqual(device.type, u"MOVA")
        self.assertFalse(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.spoof)
    def test_docomo_foma(self):
        META = {
            'HTTP_USER_AGENT': u"DoCoMo/2.0 F06B(c500;TB;W24H16)",
            'HTTP_X_DCMGUID': u"XXXXXXX",
            'REMOTE_ADDR': u"210.153.84.0",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"F06B")
        self.assertEqual(device.type, u"FOMA")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.spoof)
    def test_docomo_spoof(self):
        META = {
            'HTTP_USER_AGENT': u"DoCoMo/2.0 F06B(c500;TB;W24H16)",
            'HTTP_X_DCMGUID': u"XXXXXXX",
            'REMOTE_ADDR': u"127.0.0.1",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"F06B")
        self.assertEqual(device.type, u"FOMA")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertTrue(device.spoof)
    # KDDI
    #--------------------------------------------
    def test_kddi(self):
        META = {
            'HTTP_USER_AGENT': u"KDDI-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0",
            'HTTP_X_UP_SUBNO': u"XXXXXXX",
            'REMOTE_ADDR': u"210.230.128.224",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"SA31")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.hdml)
        self.assertFalse(device.spoof)
    def test_kddi_hdml(self):
        META = {
            'HTTP_USER_AGENT': u"SIE-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0",
            'HTTP_X_UP_SUBNO': u"XXXXXXX",
            'REMOTE_ADDR': u"210.230.128.224",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"SA31")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertTrue(device.hdml)
        self.assertFalse(device.spoof)
    def test_kddi_fake(self):
        META = {
            'HTTP_USER_AGENT': u"KDDI-SA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0",
            'HTTP_X_UP_SUBNO': u"XXXXXXX",
            'REMOTE_ADDR': u"127.0.0.1",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"SA31")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.hdml)
        self.assertTrue(device.spoof)
    
    # Softbank
    #---------------------------------------------
    def test_softbank_jphone(self):
        META = {
            'HTTP_USER_AGENT': u"J-PHONE/2.0/J-SH02",
            'HTTP_X_JPHONE_UID': u"XXXXXXX",
            'REMOTE_ADDR': u"123.108.237.0",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"J-SH02")
        self.assertEqual(device.type, u"J-PHONE")
        self.assertFalse(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.spoof)
    def test_softbank_vodafone(self):
        META = {
            'HTTP_USER_AGENT': u"Vodafone/1.0/V803T/TJ001[/Serial] Browser/VF-Browser/1.0",
            'HTTP_X_JPHONE_UID': u"XXXXXXX",
            'REMOTE_ADDR': u"123.108.237.0",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"V803T")
        self.assertEqual(device.type, u"Vodafone")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.spoof)
    def test_softbank_softbank(self):
        META = {
            'HTTP_USER_AGENT': u"SoftBank/1.0/002Pe/PJP10[/Serial] Browser/NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1",
            'HTTP_X_JPHONE_UID': u"XXXXXXX",
            'REMOTE_ADDR': u"123.108.237.0",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"002Pe")
        self.assertEqual(device.type, u"SoftBank")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertFalse(device.spoof)
    def test_softbank_softbank_fake(self):
        META = {
            'HTTP_USER_AGENT': u"SoftBank/1.0/002Pe/PJP10[/Serial] Browser/NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1",
            'HTTP_X_JPHONE_UID': u"XXXXXXX",
            'REMOTE_ADDR': u"127.0.0.1",
        }
        device = uamd.detect(META)
        self.assertEqual(device.name, u"002Pe")
        self.assertEqual(device.type, u"SoftBank")
        self.assertTrue(device.support_cookie)
        self.assertEqual(device.uid, u"XXXXXXX")
        self.assertTrue(device.spoof)
        
if __name__ == '__main__':
    unittest.main()
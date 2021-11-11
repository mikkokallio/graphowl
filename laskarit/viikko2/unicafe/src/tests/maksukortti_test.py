import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(550)
        self.assertEqual(str(self.maksukortti), "saldo: 15.5")

    def test_saldo_vahenee_oikein(self):
        testi = self.maksukortti.ota_rahaa(500)
        self.assertTrue(testi)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_saldo_ei_vahene_jos_ei_tarpeeksi_rahaa(self):
        testi = self.maksukortti.ota_rahaa(1700)
        self.assertFalse(testi)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

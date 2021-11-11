import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_paate_on_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisten_kateisosto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.kassapaate.syo_edullisesti_kateisella(250)
        palautus = self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(palautus, 160)

    def test_maukkaiden_kateisosto_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.kassapaate.syo_maukkaasti_kateisella(250)
        palautus = self.kassapaate.syo_maukkaasti_kateisella(900)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100800)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(palautus, 500)

    def test_edullisten_korttiosto_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(osto, True)
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(osto, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 4)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaiden_korttiosto_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(osto, True)
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(osto, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_negatiivinen_kortin_lataus_ei_vaikuta(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -555)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 555)
        self.assertEqual(self.maksukortti.saldo, 1555)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100555)

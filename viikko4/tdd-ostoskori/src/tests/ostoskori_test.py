import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_paivittyy(self):
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaaminen_kasvattaa_tavaroiden_maaraa_korissa(self):
        mehu = Tuote("mehu", 3)
        appelsiini = Tuote("appelsiini", 2)
        self.kori.lisaa_tuote(mehu)
        self.kori.lisaa_tuote(appelsiini)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_ostoskorin_hinta_oikein_kun_lisataan_kaksi_tuotetta(self):
        mehu = Tuote("mehu", 3)
        appelsiini = Tuote("appelsiini", 2)
        self.kori.lisaa_tuote(mehu)
        self.kori.lisaa_tuote(appelsiini)

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_tavaroiden_maara_oikein(self):
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(mehu)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(mehu)
        self.kori.lisaa_tuote(mehu)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        mehu = Tuote("mehu", 3)
        self.kori.lisaa_tuote(mehu)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "mehu")
        self.assertEqual(ostos.lukumaara(), 1)
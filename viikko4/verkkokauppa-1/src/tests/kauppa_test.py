import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 4
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "tofu", 3)
            if tuote_id == 3:
                return Tuote(3, "kaali", 1)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self.kauppa.aloita_asiointi()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_tilisiirtoa_kutsutaan_oikein_kun_ostetaan_kaksi_eri_varastossa_olevaa_tuotetta(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("maria", "11233")

        self.pankki_mock.tilisiirto.assert_called_with("maria", 42, "11233", ANY, 8)

    def test_tilisiirtoa_kutsutaan_oikein_kun_ostetaan_kaksi_samaa_varastossa_olevaa_tuotetta(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("liisa", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("liisa", 42, "11111", ANY, 10)

    def test_tilisiirtoa_kutsutaan_oikein_kun_toinen_ostettavista_tuotteista_loppu(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("liisa", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("liisa", 42, "11111", ANY, 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("liisa", "11111")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("maria", "11233")

        self.pankki_mock.tilisiirto.assert_called_with("maria", 42, "11233", ANY, 3)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("liisa", "11111")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("maria", "11233")
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("jaana", "33233")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3, ANY, ANY, ANY)

    def test_kauppa_poistaa_tuotteen_korista_ja_palauttaa_sen_varastoon(self):

        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("jaana", "33233")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)
        self.varasto_mock.palauta_varastoon.assert_called()

KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0 or not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioita = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioita):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioita] = n
            self.alkioita = self.alkioita + 1

            if self.alkioita % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioita + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

    def poista(self, n):
        for i in range(0, self.alkioita):
            if n == self.ljono[i]:
                self.ljono = self.ljono[:i] + self.ljono[i+1:]
                self.alkioita -= 1
                return True
        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioita

    def to_int_list(self):
        taulu = []
        for i in self.ljono[:self.alkioita]:
            taulu.append(i)

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        jono = str(self.ljono[:self.alkioita])
        return jono.replace('[', '{').replace(']','}')

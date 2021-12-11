from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print("--------------------------------------------")
    print("not(has at least 2 goals)")

    matcher2 = Not(
        HasAtLeast(2, "goals")
    )

    for player in stats.matches(matcher2):
        print(player)


    print("--------------------------------------------")
    print("has fewer than")

    matcher2 = HasFewerThan(2, "goals")

    for player in stats.matches(matcher2):
        print(player)

    print("--------------------------------------------")
    print("tarkistus 1")

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)

    print("--------------------------------------------")
    print("tarkistus 2")

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()

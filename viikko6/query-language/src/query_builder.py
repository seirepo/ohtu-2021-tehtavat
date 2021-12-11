from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And

class QueryBuilder:
    def __init__(self, matcher=All):
        self._matcher = matcher

    def build(self):
        return And(self._matcher)

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matcher))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matcher))

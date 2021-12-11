from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or

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

    def oneOf(self, *matchers):
        a = ()
        for matcher in matchers:
            a += (matcher,)
        
        return QueryBuilder(Or(*a))

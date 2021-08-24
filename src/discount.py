class Discount:

    def __init__(self, percents: float, visits: int) -> None:
        self._percents = percents
        self._visits = visits

    @property
    def percents(self):
        return self._percents

    @property
    def visits(self):
        return self._visits

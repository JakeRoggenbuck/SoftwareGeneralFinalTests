class Team():
    def __init__(self):
        self.number = 0
        self.name = "unknown"
        self.rookie_year = 0

    def get_display_info(self):
        return "team number is " + str(self.number)

    def print_display_info(self):
        print(self.get_display_info())

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


class Match(Team):
    def __init__(self, balls=None):
        self.balls = balls


class Calculations(Team):
    def __init__(self):
        self._matches = []

    def add_match(self, match):
        self._matches.append(match)

    def get_average_balls(self):
        total = 0
        for match in self._matches:
            total = total + match.balls
        return total/len(self._matches)


def main():
    calc = Calculations()
    while True:
        ans = input("Enter number, -1 for quit: ")
        if ans == "-1":
            break
        calc.add_match(Match(int(ans)))
    print("result " + str(calc.get_average_balls()))


if __name__ == "__main__":
    main()

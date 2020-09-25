class Team():
    def __init__(self):
        self.number = 0
        self.name = "unknown"
        self.rookie_year = 0

    def get_display_info(self):
        return "team number is " + str(self.number)

    def print_display_info(self):
        print(self.get_display_info())


class Match(Team):
    pass


class Calculations(Team):
    pass

import unittest


class MyTestCase(unittest.TestCase):
    def setup_team(self, number):
        import final_project
        self.assertTrue(True, "loaded the module")
        team = final_project.Team()
        team.number = number
        return team

    def test_team_attributes(self):
        team = self.setup_team(1678)

        team.name = "Citrus"
        team.rookie_year = 2005

        self.assertEqual(team.number, 1678, "got the team number")
        self.assertEqual(team.name, "Citrus", "got the team name")
        self.assertEqual(team.rookie_year, 2005, "got the team rookie year")

    def test_get_info_string(self):
        team = self.setup_team(1678)

        output = team.get_display_info()
        self.assertEqual(output, "team number is 1678")
        team.print_display_info()

        team.number = 254
        output = team.get_display_info()
        self.assertEqual(output, "team number is 254")
        team.print_display_info()

        for i in range(10):
            team = self.setup_team(i)
            output = team.get_display_info()
            self.assertEqual(output, "team number is " + str(i),
                             "working on interation " + str(i))


    def test_match_class(self):
        import final_project
        match = final_project.Match()
        self.assertIsInstance(match, final_project.Match)
        self.assertIsInstance(match, final_project.Team)

        match.balls = 10
        self.assertEqual(match.balls, 10, "there were 10")

    def test_calc_class(self):
        import final_project
        calc = final_project.Calculations()
        self.assertIsInstance(calc, final_project.Calculations)
        self.assertIsInstance(calc, final_project.Team)
        self.assertTrue(not isinstance(calc, final_project.Match),
                              "ensure that it's a match")

        match = final_project.Match()
        match.number = 10
        match.balls = 12
        calc.add_match(match)

        match = final_project.Match(balls=1)
        calc.add_match(match)

        number = calc.get_average_balls()
        self.assertEqual(number, 6.5, "avarge is right")


if __name__ == "__main__":
    unittest.main()

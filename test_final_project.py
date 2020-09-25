import unittest


class MyTestCase(unittest.TestCase):
    def setup_team(self):
        import final_project
        self.assertTrue(True, "loaded the module")
        team = final_project.Team()
        return team

    def test_team_attributes(self):
        team = self.setup_team()

        team.number = 1678
        team.name = "Citrus"
        team.rookie_year = 2005

        self.assertEqual(team.number, 1678, "got the team number")
        self.assertEqual(team.name, "Citrus", "got the team name")
        self.assertEqual(team.rookie_year, 2005, "got the team rookie year")

    def test_get_info_string(self):
        team = self.setup_team()
        team.number = 1678
        output = team.get_display_info()
        self.assertEqual(output, "team number is 1678")
        team.print_display_info()

    def test_match_class(self):
        import final_project
        match = final_project.Match()
        self.assertIsInstance(match, final_project.Match)
        self.assertIsInstance(match, final_project.Team)

    def test_calc_class(self):
        import final_project
        calc = final_project.Calculations()
        self.assertIsInstance(calc, final_project.Calculations)
        self.assertIsInstance(calc, final_project.Team)
        self.assertTrue(not isinstance(calc, final_project.Match),
                              "ensure that it's a match")



if __name__ == "__main__":
    unittest.main()

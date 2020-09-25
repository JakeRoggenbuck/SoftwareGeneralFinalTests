import unittest


class MyTestCase(unittest.TestCase):
    def test_team_class(self):
        import final_project
        self.assertTrue(True, "loaded the module")
        team = final_project.Team()

    def test_team_attributes(self):
        import final_project
        self.assertTrue(True, "loaded module")
        team = final_project.Team()

        team.number = 1678
        team.name = "Citrus"
        team.rookie_year = 2005

        self.assertEqual(team.number, 1678, "got the team number")
        self.assertEqual(team.name, "Citrus", "got the team name")
        self.assertEqual(team.rookie_year, 2005, "got the team rookie year")

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

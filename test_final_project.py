import unittest


class MyTestCase(unittest.TestCase):
    def test_team_class(self):
        import final_project
        self.assertTrue(True, "loaded the module")
        team = final_project.Team()

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

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


if __name__ == "__main__":
    unittest.main()

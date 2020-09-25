import unittest


class MyTestCase(unittest.TestCase):
    def test_team_class(self):
        import final_project
        team = final_project.Team()


if __name__ == "__main__":
    unittest.main()

import unittest


class Tests(unittest.TestCase):
    def test_scenario1(self):
        """
        Scenario: Multiplying by a translation matrix
          Given transform ← translation(5, -3, 2)
            And p ← point(-3, 4, 5)
           Then transform * p = point(2, 1, 7)
        """

        pass


if __name__ == "__main__":
    unittest.main()

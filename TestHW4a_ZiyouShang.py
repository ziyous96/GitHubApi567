""" author: Ziyou Shang
These are the test cases
"""
import unittest
from HW4a_ZiyouShang import get_repo, get_commits


class TestHW4a(unittest.TestCase):
    """ Test cases for HW4a """

    def test_correct_result(self):
        """ test case for checking results of valid user name """

        repos = get_repo("richkempinski")
        self.assertEqual(len(repos), 5)
        self.assertEqual(repos[0], "hellogitworld")
        self.assertEqual(repos[1], "helloworld")
        self.assertEqual(repos[2], "Mocks")
        self.assertEqual(repos[3], "Project1")
        self.assertEqual(repos[4], "threads-of-life")

        self.assertEqual(get_commits("richkempinski", repos[0]), 30)
        self.assertEqual(get_commits("richkempinski", repos[1]), 6)
        self.assertEqual(get_commits("richkempinski", repos[2]), 10)
        self.assertEqual(get_commits("richkempinski", repos[3]), 2)
        self.assertEqual(get_commits("richkempinski", repos[4]), 1)

    def test_special_cases(self):
        """ Test cases for invalid input """

        self.assertEqual(get_repo("kkk"), [])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

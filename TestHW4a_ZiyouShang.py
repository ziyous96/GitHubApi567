""" author: Ziyou Shang
These are the test cases
"""
import unittest
from unittest import mock

from HW4a_ZiyouShang import get_repo, get_commits


class TestHW4a(unittest.TestCase):
    """ Test cases for HW4a """

    # def test_correct_result(self):
    #     """ test case for checking results of valid user name """
    #
    #     repos = get_repo("richkempinski")
    #     self.assertEqual(len(repos), 5)
    #     self.assertEqual(repos[0], "hellogitworld")
    #     self.assertEqual(repos[1], "helloworld")
    #     self.assertEqual(repos[2], "Mocks")
    #     self.assertEqual(repos[3], "Project1")
    #     self.assertEqual(repos[4], "threads-of-life")
    #
    #     self.assertEqual(get_commits("richkempinski", repos[0]), 30)
    #     self.assertEqual(get_commits("richkempinski", repos[1]), 6)
    #     self.assertEqual(get_commits("richkempinski", repos[2]), 10)
    #     self.assertEqual(get_commits("richkempinski", repos[3]), 2)
    #     self.assertEqual(get_commits("richkempinski", repos[4]), 1)
    #
    # def test_special_cases(self):
    #     """ Test cases for invalid input """
    #
    #     self.assertEqual(get_repo("kkk"), [])

    @mock.patch('requests.get')
    def test_get_repos(self, mockedReq):
        """ test get_repos function using mocking """

        # normal situation
        mockedReq.return_value.text = '[{"name": "1"}, {"name": "2"}, {"name": "3"}, {"name": "4"}, {"name": "5"}]'
        repos = get_repo("someid")
        self.assertEqual(repos[0], "1")
        self.assertEqual(repos[1], "2")
        self.assertEqual(repos[2], "3")
        self.assertEqual(repos[3], "4")
        self.assertEqual(repos[4], "5")

        # when repos = 0
        mockedReq.return_value.text = '[]'
        repos = get_repo("someid")
        self.assertEqual(len(repos), 0)

    @mock.patch('requests.get')
    def test_get_commits(self, mockedReq):
        """ test get_commit function using mocking """

        # normal situation
        mockedReq.return_value.text = '[{"sha": 1}, {"sha": 2}, {"sha": 3}, {"sha": 4}, {"sha": 5}]'
        commits = get_commits("someid", "somerepo")
        self.assertEqual(commits, 5)

        # when commits = 0
        mockedReq.return_value.text = '[]'
        commits = get_commits("someid", "somerepo")
        self.assertEqual(commits, 0)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

""" author: Ziyou Shang
This is a program that take the Github user id as input and output the list of repositories of the user
with the total number of commits
"""
import ssl
import sys
import json
import requests
from math import pi, cos, sin, asin, sqrt

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_repo(userid):
    """ Function to get the data using the API """

    url = 'https://api.github.com/users/' + userid + '/repos'
    data = requests.get(url).text
    data = json.loads(data)  # get and load data from the url
    repos = []

    for repo in data:
        try:
            repos.append(repo["name"])
        except Exception as e:
            print(e)  # catch the exception when the repo cannot be found (or other cases)
            sys.exit()

    return repos


def get_commits(userid, repo):
    """ Function to get the commits of given repo """

    url = "https://api.github.com/repos/" + userid + "/" + repo + "/commits"
    data = requests.get(url).text
    data = json.loads(data)  # get and load data from the url
    commits = len(data)
    return commits


def main():
    """ The main function to get the input from the user """

    userid = input("Please enter the user id: ")
    repos = get_repo(userid)
    for repo in repos:
        commits = get_commits(userid, repo)
        print(f"Repo: {repo} Number of commits: {commits}")


if __name__ == '__main__':
    main()

import sys, os


def setup():
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + "/../src/") 


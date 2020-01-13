# GENERIC
import os
from sys import platform

# Query locations:
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
QUERY_FOLDER = ROOT_DIR + "/resources/queries/"
    
# Postgres connection string:
LOCAL_CONNECTION_STRING = "dbname='geolocator' user='postgres' host='localhost' password='postgres'"


"""
# will touch on this later. was trying to get all the sub packages on the same page

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if platform == "win32":
    QUERY_FOLDER = ROOT_DIR + "\\resources\\queries\\"
else:
    QUERY_FOLDER = ROOT_DIR + "/resources/queries/"
"""

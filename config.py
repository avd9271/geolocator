"""
This file is for containing constants that are used project wide
(such as sql connection string, query folder, etc.)

"""

# GENERIC
import os
from sys import platform

# Query locations:
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
QUERY_FOLDER = ROOT_DIR + "/resources/queries/"
    
# Postgres connection string:
LOCAL_CONNECTION_STRING = "dbname='geolocator' user='postgres' host='localhost' password='postgres'"
DOCKER_CONNECTION_STRING = "dbname='postgres' user='postgres' host='localhost' password=''"

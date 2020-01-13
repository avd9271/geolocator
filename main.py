# FLASK
from flask import Flask, request
# PROJECT
import config
from scripts.postgresclient.postgres_client import PostgresClient
from scripts.queryparser.query_parser import *

# setup:
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to basic geolocator program!"

@app.route('/run-NC-test')
def run_NC_test():
    # constants:
    query_file = 'postgis_test_no_geo_column.sql'
    connection_string = config.LOCAL_CONNECTION_STRING
    
    # init postgres client:
    pg_client = PostgresClient(connection_string)

    # read query:
    query = read_query(query_file)

    # execute sql:
    result_str = pg_client.execute_query_and_return_results_as_string(query)

    # logging
    print("results:")
    print(result_str)
    
    return format_str_for_html(result_str)


@app.route('/find-state-of-lat-lon')
def find_lat_lon_state():
    # latitude longitude setup:
    latitude = request.args.get('latitude', default=None, type = float)
    longitude = request.args.get('longitude', default=None, type = float)
    if latitude is None or longitude is None:
        return "Please input a float for latitude and longitude. format: /find-state-of-lat-lon?latitude=xxx.xx&longitude=yyy.yy"
    
    # constants:
    query_file = 'find_state_from_lat_lon.sql'
    connection_string = config.LOCAL_CONNECTION_STRING
    params = {'${LONGITUDE}': longitude, '${LATITUDE}': latitude}

    """ probably need to move this bit to a generic location """
    # init postgres client:
    pg_client = PostgresClient(connection_string)

    # read query:
    query = read_query_with_params(query_file, params)

    # execute sql:
    result_str = pg_client.execute_query_and_return_results_as_string(query)

    # logging
    print("results:")
    print(result_str)
    
    return format_str_for_html(result_str)

if __name__ == '__main__':
    app.run()

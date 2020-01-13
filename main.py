# FLASK
from flask import Flask, request
# PROJECT
import config
from scripts.postgresclient.postgres_client import PostgresClient
from scripts.queryparser.query_parser import *
from scripts.addressparser.address_parser import *

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
def run_lat_lon_state():
    # latitude longitude setup:
    latitude = request.args.get('latitude', default=None, type = float)
    longitude = request.args.get('longitude', default=None, type = float)
    if latitude is None or longitude is None:
        return "Please input a float for latitude and longitude. format: /find-state-of-lat-lon?latitude=xxx.xx&longitude=yyy.yy"
    return find_state_from_latitude_longitude(latitude, longitude)


@app.route('/find-state-from-address')
def run_address_state():
    # latitude longitude setup:
    address = request.args.get('address', default=None, type = str)
    if address is None:
        return "Please input an address. format /find-state-from-address?address='some address'"
    # lat / lon from address:
    geo_point = get_lat_lon_from_address(address)
    latitude = geo_point.latitude
    longitude = geo_point.longitude
    if latitude is None or longitude is None:
        return "Bad address input: {}".format(address)

    return find_state_from_latitude_longitude(latitude, longitude)



# ### HELPER FUNCTION ###

def find_state_from_latitude_longitude(latitude, longitude):
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

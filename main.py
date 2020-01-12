# FLASK
from flask import Flask
# PROJECT
import config
from scripts.postgresclient.postgres_client import PostgresClient
from scripts.queryparser.query_parser import read_query, format_str_for_html

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
    
    

if __name__ == '__main__':
    app.run()

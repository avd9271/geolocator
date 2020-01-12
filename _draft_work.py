import shapefile
import psycopg2

def basic_shape_file_read(filename):

    shape = shapefile.Reader(filename)

    # first shape file feature
    feature = shape.shapeRecords()[0]    
    first = feature.shape.__geo_interface__
    
    # output_
    print(first) # json format

def read_query(file_name):

    QUERY_FOLDER = 'resources/queries/'

    query_file = QUERY_FOLDER + file_name

    with open(query_file) as my_query_file:
        return my_query_file.read()


def basic_postgresql_test():

    connection_string = "dbname='geolocator' user='postgres' host='localhost' password='duvall9271'"
    query_file = 'postgis_test_no_geo_column.sql'
    query = read_query(query_file)

    try:
        connection = psycopg2.connect(connection_string)
        print("connection successful")
    except:
        print("could not connect to sql server")

    cur = connection.cursor()

    try:
        cur.execute(query)
        print("successfully executed query {}".format(query_file))
    except:
        print("could not execute query {}".format(query_file))

    rows = cur.fetchall()

    print("\nResults:")
    for row in rows:
        output = ""
        for i in range(1, len(row)):
            output += str(row[i]) + "    "
        print(output)
        

if __name__ == "__main__":

    # file_location = "resources/cb_2018_us_state_5m/cb_2018_us_state_5m.shp"

    # basic_shape_file_read(file_location)

    print("running basic sql test")
    basic_postgresql_test()


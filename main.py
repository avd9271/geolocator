import shapefile

def basic_shape_file_read(filename):

    shape = shapefile.Reader(filename)

    # first shape file feature
    feature = shape.shapeRecords()[0]    
    first = feature.shape.__geo_interface__
    
    # output_
    print(first) # json format

if __name__ == "__main__":

    file_location = "resources/cb_2018_us_state_5m/cb_2018_us_state_5m.shp"

    basic_shape_file_read(file_location)


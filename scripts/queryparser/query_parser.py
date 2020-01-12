# PROJECT
import config

QUERY_FOLDER = config.QUERY_FOLDER


def read_query(query_file):
    """
    Idea behind this file is that you would have some more functionality
    than just reading a file.

    Such as inputing parameters into parameterized queries
    """

    query_path = QUERY_FOLDER + query_file
    
    with open(query_path) as q_file:
        return q_file.read()

def format_str_for_html(result_str):

    new_str = "<pre>" + result_str + "</pre>"

    return new_str

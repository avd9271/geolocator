# POSTGRES
import psycopg2

class PostgresClient:

    def __init__(self, connection_string):
        # get connection string from input
        self.connection_string = connection_string

        # set connection
        try:
            self.connection = psycopg2.connect(connection_string)
            print("Connection to SQL server successful")
        except Exception as e:
            message = "Error connecting to SQL server: {}".format(str(e))
            raise PostgresClientConnectionException(message)

        # set cursor
        self.cursor = self.connection.cursor()

    def execute_query_and_return_results(self, query):
        print("Running query {}".format(query))

        try:
            self.cursor.execute(query)
            print("Sucessfully executed query")
        except Exception as e:
            message = "Error running SQL query: {}".format(str(e))
            raise PostgresClientQueryException(message)
        return self.cursor.fetchall()

    def execute_query_and_return_results_as_string(self, query):
        results = self.execute_query_and_return_results(query)

        output = ""
        # cycle through results and add to output string
        for row in results:
            for i in range(0, len(row)):
                output += str(row[i]) + "\t"
            output += "\n"
        return output

# ### EXCEPTION CLASSES ###

class PostgresClientConnectionException(Exception):

    def __init__(self, message):
        self.message = message

class PostgresClientQueryException(Exception):

    def __init__(self, message):
        self.message = message

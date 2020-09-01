import pymongo
from multiprocessing import Pipe, Process
from importlib import reload
from datetime import date
import time

today = date(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday).isoformat()


def establish_connection():
    client = pymongo.MongoClient('localhost', 27017)

    # Accessing database
    db = client.CarDatabase

    # Getting collection
    collection = db.CarDatabase

    return collection


def searched_today():
    """
    Method checking if search for particular car model was done in current day.
    :return:
    """
    from UI import user_input
    if establish_connection().find_one({"MAKE": user_input[0], "MODEL": user_input[1], "FIRST_SEARCH": today}) is not None:
        return True
    else:
        return False


def add_to_database():
    """
    Method adding web results for particular car models
    :return:
    """
    if searched_today() is True:
        print('Search for this car model was already done today')
    else:
        establish_connection().insert_many(create_entry_receiver())


def query_database():
    """
    Method returning results from database according to make and model which user specified
    :return:
    """
    from UI import user_input
    import calculations
    reload(calculations)
    calculations.average()
    print('Hello Database!: ', user_input, '\n')

    # TESTING - Printing all of the cars existing in a database (in respect to make and model user specified)
    # criteria = establish_connection().find({"MAKE": user_input[0], "MODEL": user_input[1]})
    # for post in criteria:
    #     print(post)


def create_entry_receiver():
    """
    :return: function receiving results of create_entry_sender method from parser.py, initialising process with that
    ULTIMATELY - imputing this data to database
    method
    """
    import parser
    reload(parser)
    empty = []

    parent_conn, child_conn = Pipe()
    p = Process(target=parser.create_entry_sender, args=(child_conn,))
    p.start()
    empty.extend(parent_conn.recv())

    if not empty:
        print("Car you're looking for doesn't exist in our database")
    else:
        return empty


def run_plot():
    """
    execution of plot_bar_show method
    :return:
    """
    import plot
    plot.plot_bar_show()
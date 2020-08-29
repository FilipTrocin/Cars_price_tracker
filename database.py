import pymongo
import UI
from multiprocessing import Pipe, Process
from importlib import reload


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
    pass


def query_database():
    """
    Method returning results from database according to make and model which user specified
    :return:
    """
    print('Hello Database!: ', UI.user_input)
    user_search = UI.user_input
    criteria = establish_connection().find({"MAKE": user_search[0], "MODEL": user_search[1]})

    for post in criteria:
        print(post)


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
        print(empty)

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

    # inserting object to database, adding _id automatically
    # new = collection.insert_many(post)


# Temporary function to checking is data from UI.global_list is transferred to database.py
def print_grabber():
    """
    ULTIMATELY - queering by this data from database
    :return:
    """
    print('Hello Database!: ', UI.user_input)


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

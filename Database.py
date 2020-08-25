import pymongo
import UI
from multiprocessing import Pipe, Process
import Parser


def establish_connection():
    client = pymongo.MongoClient('localhost', 27017)

    # Accessing database
    db = client.CarDatabase

    # Getting collection
    collection = db.CarDatabase

    # inserting object to database, adding _id automatically
    # new = collection.insert_many(post)


# Temporary function to checking is data from UI.global_list is transferred to Database.py
def print_grabber():
    print('Hello Database!: ', UI.user_search_list)


def create_entry_receiver():
    """
    :return: function receiving results of create_entry_sender method from Parser.py, initialising process with that
    method
    """
    parent_conn, child_conn = Pipe()
    p = Process(target=Parser.create_entry_sender, args=(child_conn,))
    p.start()
    print(parent_conn.recv())

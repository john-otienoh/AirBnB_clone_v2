#!/usr/bin/python3
"""

"""
from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    """
    It’s time to change your storage engine and use SQLAlchemy
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the class
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

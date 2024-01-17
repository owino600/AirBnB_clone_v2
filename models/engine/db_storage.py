from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = None
        self.__session = None

        user = os.environ.get(HBNB_MYSQL_USER)
        password = os.environ.get(HBNB_MYSQL_PWD)
        host = os.environ.get(HBNB_MYSQL_HOST, localhost)
        database = os.environ.get(HBNB_MYSQL_DB)
        env = os.environ.get(HBNB_ENV)
        self.__engine = create_engine('mysql+mysqldb://hbnb_dev@localhost/hbnb_dev_db', pool_pre_ping=True)

        if env == 'test':
            self.__engine.execute("DROP TABLE IF EXISTS {}".format(', '.join(self.all().keys())))

            def new(self, obj):
                if obj:
                    self.__session.add(obj)

            def save(self):
                self.__session.save(obj)

            def delete(self, obj=None):
                if obj:
                    self.__session.delete(obj)
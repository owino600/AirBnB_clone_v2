from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = None

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
                self.__session.commit(obj)

            def delete(self, obj=None):
                if obj:
                    self.__session.delete(obj)

            def reload(self):
                Base.metadata.create_all(engine)
                self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)

            def all(self, cls=None):
                if cls:
                    obj = self.__session.query(self.classes()[cls])
                else:
                    obj = self.__session.query(User).all()
                    obj = self.__session.query(State).all()
                    obj = self.__session.query(City).all()
                    obj = self.__session.query(Amenity).all()
                    obj = self.__session.query(Place).all()
                    obj = self.__session.query(Review).all()
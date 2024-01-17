#!usr/bin/python3
import unittest
import MySQLdb
from models.user import User
from models import storage
import os

class TestDBStorage(unittest.TestCase):
    """test the dbstorage engine"""
    def test_new_save(self):
        db = MySQLdb.connect(user=os.environ.get(HBNB_MYSQL_USER), host=os.environ.get(HBNB_MYSQL_HOST, localhost), passwd=os.environ.get(HBNB_MYSQL_PWD), db=os.environ.get(HBNB_MYSQL_DB) ,port=3306)

        cus = db.cusor()
        cus.execute('SELECT COUNT(*) FROM users')
        count = cus.fetchall()
        cus.close()
        db.close()
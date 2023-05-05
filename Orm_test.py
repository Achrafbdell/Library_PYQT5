from peewee import *
db = MySQLDatabase('my_app', user='root', password='toor',
                         host='localhost', port=3306)

class Person(Model):
    name=CharField()
    birthday= DateField()

    class Meta:
        database = db



db.connect()
db.create_tables([])
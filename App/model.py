import datetime
import os
from peewee import *

path_to_database = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.db')
sqlt_database = SqliteDatabase(path_to_database, pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = sqlt_database


class Markets(BaseModel):
    name = CharField(max_length=100)
    adress = CharField(max_length=100)


class Users(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    default_market = ForeignKeyField(Markets, backref='users')
    admin = BooleanField(default=True)


class ProductGroup(BaseModel):
    name = CharField(max_length=100)


class Product(BaseModel):
    name = CharField(unique=True)
    id_from1c = CharField(max_length=11)
    group = ForeignKeyField(ProductGroup, backref='products')


class Tare(BaseModel):
    name = CharField(unique=True)


class Base(BaseModel):
    name = CharField(max_length=3)


class ColorCard(BaseModel):
    card_id = CharField(max_length=20, unique=True)
    name = CharField(max_length=50)


class Color(BaseModel):
    color_id = CharField(max_length=20)
    color_card = ForeignKeyField(ColorCard, backref='colors')


class ProductReference(BaseModel):
    product = ForeignKeyField(Product, backref='product_references')
    tare = ForeignKeyField(Tare, backref='product_references')
    base = ForeignKeyField(Base, backref='product_references')


class Log(BaseModel):
    date = DateTimeField(default=datetime.datetime.now(), formats='%Y-%m-%d %H:%M:%S')
    phone = CharField(max_length=15)
    market = ForeignKeyField(Markets, backref='logs')
    exported = BooleanField(default=False)


class LogTablePart(BaseModel):
    log_id = ForeignKeyField(Log, backref='logtableparts')
    row_number = IntegerField(null=False, index=True)
    product = ForeignKeyField(Product, backref='logtableparts')
    tare = ForeignKeyField(Tare, backref='logtableparts')
    base = ForeignKeyField(Base, backref='logtableparts')
    color = ForeignKeyField(Color, backref='logtableparts')


class CurrentSettings(BaseModel):
    current_user = ForeignKeyField(Users, backref='users')
    current_market = ForeignKeyField(Markets, backref='markets')
    param1 = CharField()
    param2 = CharField()
    param3 = CharField()


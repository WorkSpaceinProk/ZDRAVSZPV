import pytest
import requests

from lxml import etree as et
from lxml.builder import ElementMaker
from bs4 import BeautifulSoup

from resources import *
import psycopg2

conn = psycopg2.connect(dbname="PostgreSQL 14", host="10.50.3.41", user="n3tester", password="xgCZ2aekU7znSGfSkui3", port="5433")
print("Подключение установлено")
conn.close()

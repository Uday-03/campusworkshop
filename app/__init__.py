"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaadpqk728r886bnoig-a.oregon-postgres.render.com",
        database="todo_list_zr6a",
        user="todo_list_zr6a_user",
        password="ORuQyRtYkuU9V0BTHDHM6j7VCFO1DBv2")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

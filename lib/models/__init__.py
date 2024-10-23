import sqlite3

CONN = sqlite3.connect('animal_trivia.db')
CURSOR = CONN.cursor()

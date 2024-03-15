import sqlite3

banco = sqlite3.connect('db.sqlite3')

cursor = banco.cursor()

cursor.execute("""
    DROP DATABASE db.sqlite3
""")

banco.commit()
banco.close()
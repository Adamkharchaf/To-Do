from peewee import *

db = SqliteDatabase("todo.db")

class Task(Model):
    title = CharField(max_length=100)
    description = TextField()
    due_date = DateField(formats='%Y-%m-%d') # 2025-03-8
    status = BooleanField(default=False)

    class Meta :
        database = db
if __name__ == "__main__":
    db.connect()
    db.create_tables([Task])
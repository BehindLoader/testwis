import peewee

db = peewee.SqliteDatabase('database.db')

class Value(peewee.Model):
    id = peewee.AutoField()
    name = peewee.CharField(
        verbose_name = 'Название'
    )
    value = peewee.FloatField(
        verbose_name = 'Значение'
    )
    date = peewee.DateField(
        verbose_name = 'Дата'
    )
    class Meta:
        database = db

if __name__ == '__main__':
    Value.create_table()
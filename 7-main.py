from faker import Faker
from datetime import datetime
import sqlite3

fake_data = Faker()

name = fake_data.name();
address = fake_data.address();
email = fake_data.email();
city = fake_data.city();
phone = fake_data.phone_number();
country = fake_data.country();
age = fake_data.date_of_birth();

con = sqlite3.connect('databasefile.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS table1 (name text, address text, email text, city text, phone text, country text, age text)''')
for i in range(1,200):
    cur.execute('INSERT INTO table1 VALUES (:name, :address, :email, :city, :phone, :country, :age)',
        {'name': fake_data.name(), 'address': fake_data.address(), 'email': fake_data.email(), 'city': fake_data.city(), 'phone': fake_data.phone_number(), 'country': fake_data.country(), 'age': fake_data.date_of_birth()}
        )

cur.execute('SELECT * FROM table1')

for i in cur.execute('SELECT name, age FROM table1 limit 20'):
    print(i)

con.commit()
con.close()
import sqlite3
from datetime import datetime
con = sqlite3.connect('social_network.db')
cur = con.cursor()

add_person_query = """
    INSERT INTO people
    (
        name,
        email,
        address,
        city,
        province,
        country,
        phone,
        bio,
        age,
        created_at,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

new_person = ('Bob Loblaw',
             'bob.loblaw@whatever.net',
             '123 Fake St.',
             'Fakesville',
             'Fake Edward Island',
             'Fakopolis',
             '705-123-4567',
             'Enjoys making funny sounds when talking.',
             46,
             datetime.now(),
             datetime.now())
# Execute query to add new person to people table
cur.execute(add_person_query, new_person)
con.commit()
con.close()
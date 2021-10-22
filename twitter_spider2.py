# INTEGER PRIMARY KEY - automatically adds the key value for any row we insert into a table
# A logical key is a key that the “real world” might use to look up a row-
# -In our example data model, the name field is a logical key.
# A primary key is usually a number that is assigned automatically by the database-
# -It generally has no meaning outside the program and is only used to link rows from different tables together
# A foreign key is usually a number that points to the primary key of an-
# -associated row in a different table. An example of a foreign key in our data model is the from_id.

import json
import sqlite3
import requests
import os

bearer_token = os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/1.1/followers/list.json"
conn = sqlite3.connect('version2.sqlite')
cur = conn.cursor()

# The People table has an additional column to store the numeric key,
# associated with the row for this Twitter user
cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
# in creating this Follows table, we are modelling a “relationship” where
# one person “follows” someone else and representing it with a pair of numbers indi-
# cating that (a) the people are connected and (b) the direction of the relationship
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if acct == 'quit': break
    if len(acct) < 1:
        cur.execute('SELECT id, name FROM People WHERE retrieved=0 LIMIT 1')
        try:
            id, acct = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)''', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid

    query_params = {'screen_name': acct, 'count': 20}
    print('Retrieving account', acct)
    # Method required by bearer token authentication.

    # ################ Twitter authentication ########################

    def bearer_oauth(r):
        r.headers["Authorization"] = f"Bearer {bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r


    def connect_to_endpoint(url, params):
        response = requests.get(url, auth=bearer_oauth, params=params)
        x = response.status_code, response.headers
        resp = open('resp.json', 'w')
        resp.write(str(x))
        resp.close()
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()


    json_response = connect_to_endpoint(search_url, query_params)
    data = json.dumps(json_response, indent=1)
    js = json.loads(data)

    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    # ################ End of Twitter authentication ########################

    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))
    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)''', (friend, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

# ################ Quering from the database ########################

cur.execute('SELECT * FROM People')
count = 0
print('People:')
for row in cur:
    if count < 5:
        print(row)
    count = count + 1
print(count, 'rows.')

cur.execute('SELECT * FROM Follows')
count = 0
print('Follows:')
for row in cur:
    if count < 5:
        print(row)
    count = count + 1
print(count, 'rows.')

cur.execute('''SELECT * FROM Follows JOIN People ON Follows.to_id = People.id WHERE Follows.from_id = 2''')
count = 0
print('Connections for id=2:')
for row in cur:
    if count < 5:
        print(row)
    count = count + 1
print(count, 'rows.')

cur.close()

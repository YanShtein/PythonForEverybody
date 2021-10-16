import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('sql2.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'Library.xml'


# Loop throung all the children in this outer dictionary, and find a child tag that has a particular key.
# the key for the object is inside an object in the xml file...
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(file_name)
all_dict = stuff.findall('dict/dict/dict')
print('Dict count:', len(all_dict))
for entry in all_dict:
    if lookup(entry, 'Track ID') is None: continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    if name is None or artist is None or album is None: continue

    print(name, artist, album, count, rating, length)
    # as Artist-> name is unique, -IGNORE- means if there will be an attempt to insert same name twice, it will blow up.
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))     # a way to have one tuple
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, len, rating, count) VALUES (?, ?, ?, ?, ?)''',
                (name, album_id, length, rating, count))

    conn.commit()

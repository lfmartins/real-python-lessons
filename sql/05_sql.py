import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	for firstname, lastname in c.execute('SELECT firstname, lastname FROM employees'):
		print('{} {}'.format(firstname, lastname))
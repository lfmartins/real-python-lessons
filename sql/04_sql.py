import sqlite3
import csv

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()
	c.execute('CREATE TABLE  employees (firstname TEXT, lastname TEXT)')
	employees = csv.reader(open('employees.csv', 'rU'))
	c.executemany('INSERT INTO employees(firstname, lastname) values (?, ?)',
				  employees)
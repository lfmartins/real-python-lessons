import sqlite3

connection = sqlite3.connect('cars.db')
c = connection.cursor()

c.execute("""
	CREATE TABLE orders (
		make TEXT, 
		model TEXT, 
		order_date TEXT)""")

orders = [
	( 'Ford', 'Taurus', '2017-03-01'),
	( 'Ford', 'Taurus', '2017-04-02'),
	( 'Ford', 'Mustang', '2017-05-03'),
	( 'Honda', 'Accord', '2017-01-02'),
	( 'Honda', 'Accord', '2017-06-15'),
	( 'Honda', 'Accord', '2017-10-13'),
	( 'Honda', 'Civic', '2017-05-23'),
	( 'Honda', 'Civic', '2017-02-28'),
	( 'Honda', 'Civic', '2017-12-09'),
	( 'Honda', 'CR-V', '2017-08-08'),
	( 'Honda', 'CR-V', '2017-09-14'),
	( 'Honda', 'CR-V', '2017-06-15'),
]

c.executemany("""
		INSERT INTO orders VALUES(?, ?, ?)""",
		orders)

connection.commit()

c.execute("""
	SELECT inventory.Make, inventory.Model, inventory.quantity, orders.order_date
	FROM inventory, orders
	WHERE inventory.Make = orders.make AND inventory.Model = orders.model""")

rows = c.fetchall()

for make, model, quantity, order_date in rows:
	print('Car: {} {}\n   Quantity: {}\n   Date: {}\n'.format(
		make, model, quantity, order_date))



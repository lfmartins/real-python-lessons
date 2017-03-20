import sqlite3

connection = sqlite3.connect('cars.db')
c = connection.cursor()

data = [
	( 'Ford', 'Taurus', 120),
	( 'Ford', 'Mustang', 40),
	( 'Honda', 'Accord', 110),
	( 'Honda', 'Civic', 86),
	( 'Honda', 'CR-V', 45),
]

c.executemany("""
	INSERT INTO inventory(Make, Model, Quantity) 
	VALUES (?, ?, ?)""", 
	data)

print('\nInitial Inventory:\n')

rows = c.execute("""
	SELECT * FROM inventory """)

for make, model, quantity in rows:
	print(make, model, quantity)

c.execute("""
	UPDATE inventory
	SET quantity=87
	WHERE Model='Accord' """)

c.execute("""
	UPDATE inventory
	SET quantity=32
	WHERE Model='Mustang' """)

print('\n\nFord Vehicles:\n')

rows = c.execute("""
	SELECT Model, Quantity
	FROM inventory
	WHERE Make='Ford' """)

for model, quantity in rows:
	print(model, quantity)

connection.commit()
connection.close()

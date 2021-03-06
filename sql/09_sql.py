import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("""
		SELECT population.city, population.population, regions.region
		FROM population, regions
		WHERE population.city = regions.city""")

	rows = c.fetchall()

	for city, population, region in rows:
		print(city, population, region)

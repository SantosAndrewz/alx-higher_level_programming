-- lists all the cities contained in the database hbtn_0d_usa
-- lists all rows of a given column in the database.
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC

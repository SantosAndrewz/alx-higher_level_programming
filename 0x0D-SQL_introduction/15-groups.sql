-- lists the number of recors with the same score in the table second_table in the hbtn_0c_0 database.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC

-- lists all the records of the table second_table of the hbtn_0c_0 without listing rows missing a  name value.
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC

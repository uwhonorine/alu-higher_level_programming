-- Lists the best records (score 10+), best score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

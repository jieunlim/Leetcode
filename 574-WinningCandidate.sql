# Write your MySQL query statement below
SELECT name
FROM(
    SELECT name, DENSE_RANK() OVER(ORDER BY COUNT(candidateId) DESC ) ranking
    FROM VOTE v
    JOIN Candidate c ON v.candidateId = c.id
    GROUP BY candidateId
)a

WHERE a.ranking = 1

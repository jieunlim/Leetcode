# # Write your MySQL query statement below
SELECT team_name,
    count(*) as matches_played, 
    sum(CASE WHEN home_team_goals>away_team_goals THEN 3 WHEN home_team_goals = away_team_goals THEN 1 else 0 END) as points,
    sum(home_team_goals) as goal_for, 
    sum(away_team_goals) as goal_against, 
    sum(home_team_goals) - sum(away_team_goals) as goal_diff
    
FROM(
    SELECT home_team_id, home_team_goals, away_team_goals
    FROM Matches
    UNION ALL
    SELECT away_team_id as home_team_id, away_team_goals as home_team_goals, home_team_goals as away_team_goals
    FROM Matches
) g
JOIN Teams t ON g.home_team_id = t.team_id 
GROUP BY team_name
ORDER BY 3 DESC, 6 DESC, 1

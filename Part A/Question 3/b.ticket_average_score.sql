SELECT
    external_ticket_id,
    Round(AVG(score),2) AS average_score
FROM
    autoqa_ratings
GROUP BY
    external_ticket_id;

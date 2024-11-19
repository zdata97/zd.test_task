WITH rating_scores AS (
    SELECT
        review_id,
        CASE
            WHEN SUM(weight) > 0 THEN
                (SUM((rating * 1.0 / rating_max) * weight) / SUM(weight)) * 100
            ELSE NULL
        END AS rating_score
    FROM
        manual_ratings
    WHERE
        rating != 42 
    GROUP BY
        review_id
)

SELECT
    review_id,
    CONCAT(ROUND(rating_score, 2), '%') AS rating_score
FROM
    rating_scores;

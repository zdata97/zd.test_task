WITH reviewee_scores AS (
    SELECT
        reviewee_id,
        COUNT(review_id) AS review_count,
        Round(AVG(score),2) AS average_score
    FROM
        manual_reviews
    GROUP BY
        reviewee_id
)
SELECT
    reviewee_id,
    average_score
FROM
    reviewee_scores
WHERE
    review_count >= 2;

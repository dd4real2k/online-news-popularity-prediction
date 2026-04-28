-- analysis_queries.sql
-- SQL Analysis for Online News Popularity Project

-- 1. Preview dataset
SELECT *
FROM news
LIMIT 5;


-- 2. Basic dataset overview
SELECT
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares,
    MIN(shares) AS minimum_shares,
    MAX(shares) AS maximum_shares
FROM news;


-- 3. Most popular article categories
SELECT
    CASE
        WHEN data_channel_is_lifestyle = 1 THEN 'Lifestyle'
        WHEN data_channel_is_entertainment = 1 THEN 'Entertainment'
        WHEN data_channel_is_bus = 1 THEN 'Business'
        WHEN data_channel_is_socmed = 1 THEN 'Social Media'
        WHEN data_channel_is_tech = 1 THEN 'Technology'
        WHEN data_channel_is_world = 1 THEN 'World'
        ELSE 'Other'
    END AS category,
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news
GROUP BY category
ORDER BY average_shares DESC;


-- 4. Weekday popularity analysis
SELECT
    CASE
        WHEN weekday_is_monday = 1 THEN 'Monday'
        WHEN weekday_is_tuesday = 1 THEN 'Tuesday'
        WHEN weekday_is_wednesday = 1 THEN 'Wednesday'
        WHEN weekday_is_thursday = 1 THEN 'Thursday'
        WHEN weekday_is_friday = 1 THEN 'Friday'
        WHEN weekday_is_saturday = 1 THEN 'Saturday'
        WHEN weekday_is_sunday = 1 THEN 'Sunday'
    END AS weekday,
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news
GROUP BY weekday
ORDER BY average_shares DESC;


-- 5. Image usage and article popularity
SELECT
    CASE
        WHEN num_imgs = 0 THEN 'No images'
        WHEN num_imgs BETWEEN 1 AND 3 THEN '1-3 images'
        WHEN num_imgs BETWEEN 4 AND 7 THEN '4-7 images'
        ELSE '8+ images'
    END AS image_group,
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news
GROUP BY image_group
ORDER BY average_shares DESC;


-- 6. Video usage and article popularity
SELECT
    CASE
        WHEN num_videos = 0 THEN 'No videos'
        WHEN num_videos BETWEEN 1 AND 2 THEN '1-2 videos'
        WHEN num_videos BETWEEN 3 AND 5 THEN '3-5 videos'
        ELSE '6+ videos'
    END AS video_group,
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news
GROUP BY video_group
ORDER BY average_shares DESC;


-- 7. Article length and popularity
SELECT
    CASE
        WHEN n_tokens_content < 500 THEN 'Short articles'
        WHEN n_tokens_content BETWEEN 500 AND 1000 THEN 'Medium articles'
        ELSE 'Long articles'
    END AS article_length_group,
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news
GROUP BY article_length_group
ORDER BY average_shares DESC;


-- 8. Keyword count and popularity
SELECT
    num_keywords,
    COUNT(*) AS total_articles,
    ROUND(AVG(shares), 2) AS average_shares
FROM news
GROUP BY num_keywords
ORDER BY average_shares DESC;


-- 9. Top 10 articles by shares
SELECT
    shares,
    n_tokens_title,
    n_tokens_content,
    num_imgs,
    num_videos,
    num_keywords
FROM news
ORDER BY shares DESC
LIMIT 10;


-- 10. High-performing articles above average shares
SELECT
    COUNT(*) AS articles_above_average
FROM news
WHERE shares > (
    SELECT AVG(shares)
    FROM news
);

SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE T.creation > DATE_SUB(NOW(), INTERVAL 7 DAY) GROUP BY R.rid ORDER BY SUM(T.vote) DESC;
SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid WHERE T.creation > DATE_SUB(NOW(), INTERVAL 7 DAY) GROUP BY R.rid ORDER BY SUM(T.vote) DESC;

SELECT R.rid, SUM(T.vote) FROM restaurants R LEFT JOIN transactions T ON R.rid=T.rid GROUP BY R.rid ORDER BY SUM(T.vote) DESC;
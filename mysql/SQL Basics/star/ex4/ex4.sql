-- SELECT full_name FROM imdb.actors;
-- SELECT COUNT(title) FROM movies ; --//  38 
-- SELECT COUNT(title) FROM movies WHERE genre = "action" -- // 3
 -- SELECT COUNT(title) FROM movies WHERE NOT genre = "action" -- // 34
 -- SELECT COUNT(title) FROM movies WHERE year = "2000" -- // 5

-- ● How many movie titles have the word “the” in them?
-- SELECT COUNT(title) FROM movies WHERE title LIKE '%the%'	-- // 5

-- ● How many movie titles start with the word “the”?
SELECT COUNT(title) FROM movies WHERE title LIKE 'the%' 
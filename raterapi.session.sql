
/* GAMES WITH MORE THAN 3 PLAYERS */
-- SELECT g.title title
-- FROM raterapi_game g
-- WHERE g.number_of_players > 3


/* WHAT IS THE MOST REVIEWED GAME? */
-- SELECT MAX(number_of_reviews) review_count, title 
-- FROM
-- (SELECT g.title title, COUNT(r.id) number_of_reviews
-- FROM raterapi_reviews r 
-- JOIN raterapi_game g on g.id = r.game_id
-- GROUP BY g.id )


-- /* CHILDREN UNDER 8 */
-- SELECT g.title title
-- FROM raterapi_game g
-- WHERE g.age < 8

                SELECT
                    g.title Title,
                    AVG(r.rating) AverageRating,
                    g.id game_id
                FROM
                    raterapi_game g
                JOIN
                    raterapi_ratings r ON r.game_id = g.id
                GROUP BY g.id
                ORDER BY AverageRating DESC
                LIMIT 5

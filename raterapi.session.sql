                SELECT
                    gc.id,
                    c.name CategoryName,
                    COUNT(g.id) NumberGames
                FROM raterapi_categories c 
                JOIN raterapi_game_categories gc ON gc.categories_id = c.id
                JOIN raterapi_game g ON g.id = gc.game_id
                GROUP BY c.id

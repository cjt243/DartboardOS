-- game line table
CREATE TABLE IF NOT EXISTS game_line (
 id integer PRIMARY KEY,
 game_id integer,
 datetimestamp datetime,
 hit text,
 points integer,
 player_id integer,
 FOREIGN KEY (game_id) REFERENCES game_header (id),
 FOREIGN KEY (player_id) REFERENCES player (id)
);

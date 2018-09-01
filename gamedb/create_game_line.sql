-- game line table
CREATE TABLE IF NOT EXISTS game_line (
 id integer PRIMARY KEY,
 FOREIGN KEY (game_id) REFERENCES game_header (id)
 datetimestamp datetime,
 hit text,
 points integer,
 FOREIGN KEY (player_id) REFERENCES player (id)
);

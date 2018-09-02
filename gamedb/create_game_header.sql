-- game header table
CREATE TABLE IF NOT EXISTS game_header (
 id integer PRIMARY KEY,
 game_type text,
 game_start datetime,
 game_end datetime,
 player1_id integer,
 player2_id integer,
 winner_id integer,
 player1_score integer,
 player2_score integer,
 FOREIGN KEY (player1_id) REFERENCES player (id),
 FOREIGN KEY (player2_id) REFERENCES player (id),
 FOREIGN KEY (winner_id) REFERENCES player (id)
);

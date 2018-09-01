-- player table
CREATE TABLE IF NOT EXISTS player (
  id integer PRIMARY KEY,
  username text,
  create_date date,
);

-- game header table
CREATE TABLE IF NOT EXISTS game_header (
 id integer PRIMARY KEY,
 game_type text,
 game_start datetime,
 game_end datetime,
 FOREIGN KEY (player1_id) REFERENCES player (id)
 FOREIGN KEY (player2_id) REFERENCES player (id)
 FOREIGN KEY (winner_id) REFERENCES player (id)
 player1_score integer,
 player2_score integer
);

-- game line table
CREATE TABLE IF NOT EXISTS game_line (
 id integer PRIMARY KEY,
 FOREIGN KEY (game_id) REFERENCES game_header (id)
 datetimestamp datetime,
 hit text,
 points integer,
 FOREIGN KEY (player_id) REFERENCES player (id)
);

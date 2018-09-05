Select a.id,
			a.game_type,
			a.game_start,
			a.game_end,
			p1.username as player1,
			p2.username as player2,
			w.username as winner,
			a.player1_score,
			a.player2_score		
From game_header a
left join player p1 on (a.player1_id=p1.id)
left join player p2 on (a.player2_id=p2.id)
left join player w on (a.winner_id=w.id)
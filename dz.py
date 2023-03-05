chess_players = {
"Carlsen, Magnus": 1865,
"Firouzja, Alireza": 2804,
"Ding, Liren": 2799,
"Caruana, Fabiano": 1792,
"Nepomniachtchi, Ian": 2773
}


new_list = {n: item for item, n in chess_players.items()}
new_list_1 = {n: item for item, n in chess_players.items() if n >= 2000}

print(new_list)
print(new_list_1)

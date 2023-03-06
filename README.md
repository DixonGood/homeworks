chess_players = {
"Carlsen, Magnus, Name": 1865,
"Firouzja, Alireza, Work": 2804,
"Ding, Liren, Lucen": 2799,
"Caruana, Fabiano, Flamingo": 1792,
"Nepomniachtchi, Ian, Good": 2773
}


new_list = {n: item for item, n in chess_players.items()}
new_list_1 = {n: item for item, n in chess_players.items() if n >= 2000}

print(new_list)
print(new_list_1)
print('-' * 50)

chess_players_2 = {
'77, 14, 16' : 1865,
'95, 90, 17' : 2804,
'182, look, 15' : 2799,
'19, cool, 14' : 1792,
'done, 99, work': 2773
}

new_list_2 = {j: good for good, j in chess_players_2.items()}
print(new_list_2)

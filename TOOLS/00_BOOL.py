"BOOL"  #


"РЕДУВА ИГРАЧИТЕ"
player_1_turn = True
shoot_number = int(input())
for _ in range(shoot_number):
    if player_1_turn:  # Player two coords are reversed for no reason
        print("Player 1 shoot")
    else:
        print("Player 2 shoot")
    player_1_turn = not player_1_turn

"""
Battle Boats
You and your best friend are so bored of writing code whole day and
decide to play a game of battle boats.
After a few games played you felt bored again and since you are already a programmer
geek you decide to implement it using all your skills acquired during the last
couple of weeks.

The first player to Shoot is Player 1
Input

    Read from the standard input
    On the first line, find R and C, separated by a space
        The size of the board of each player (they are equal)
        R rows, C columns
    On the next 2*R rows, find the numbers 1 or 0 as a value of every cell of the board of each player.
        The first R lines are for player one's and the next R lines are for player two's board.
    After that you will receive a sequence of commands
        Each on a new line until you reach END
        The commands will be in the format [Shoot R C] where:
            R is the row on which you put your bomb
            C is the column on which you put your bomb
            R and C define the cell

Output

    Print on the standard output
        Booom
        Missed
        You already shot there!
    On the last line you should print the result of every player (boats left undestroyed) int format P1:P2

Example

2 2
0 1
1 1
1 0
1 1
Shoot 1 1
Shoot 0 1
Shoot 0 0
Shoot 0 0
Shoot 1 1
Shoot 1 0
END

Output:

Booom
Booom
Booom
Missed
You already shot there!
Booom
1:1


Sample tests
Input
2 2
0 1
1 1
1 0
1 1
Shoot 1 1
Shoot 0 1
Shoot 0 0
Shoot 0 0
Shoot 1 1
Shoot 1 0
END

Output
Booom
Booom
Booom
Missed
You already shot there!
Booom
1:1


Input
3 4
0 1 1 1
1 1 0 0
1 1 0 1
1 0 1 1
1 0 0 0
1 1 1 1
Shoot 2 3
Shoot 1 1
Shoot 2 1
Shoot 0 0
Shoot 1 1
Shoot 1 1
Shoot 2 1
Shoot 2 3
END

Output
Booom
Booom
Booom
Missed
Missed
You already shot there!
You already shot there!
Booom
6:6


Input
2 2
0 0
1 0
0 1
0 1
Shoot 1 1
END

Output
Missed
1:2
"""


def count_result(bord_name):
    counter = 0
    for row in bord_name:
        for el in row:
            if el == 1:
                counter += 1
    return counter


row_num, col_num = [int(x) for x in input().split(" ")]

bord_p1 = []
for row in range(row_num):
    bord_p1.append([int(el) for el in input().split()])

bord_p2 = []
for row in range(row_num - row_num):
    col_cord = ([int(el) for el in input().split()])
    for el in col_cord:
        el = el - col_num

command = input()
player_turn = 0

while command != "END":
    coordinates = command.split(" ")
    row_cord = int(coordinates[1])
    col_cord = int(coordinates[2])

    if player_turn % 2 == 0:
        if bord_p2[row_cord][col_cord] == 1:
            bord_p2[row_cord][col_cord] = 2
            print("Booom")
        elif bord_p2[row_cord][col_cord] == 0:
            print('Missed')
        else:
            print("You already shot there!")
        player_turn += 1

    else:
        if bord_p1[row_cord][col_cord] == 1:
            bord_p1[row_cord][col_cord] = 2
            print("Booom")
        elif bord_p1[row_cord][col_cord] == 0:
            print('Missed')
        else:
            print("You already shot there!")
        player_turn += 1

    command = input()

result_p1 = count_result(bord_p1)
result_p2 = count_result(bord_p2)

print(f"{result_p1}:{result_p2}")

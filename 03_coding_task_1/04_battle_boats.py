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


def read_player_board(rows):
    player = []
    for _ in range(rows):
        player.append(input().split())
    return player


def read_coordinates():
    commands_list = []
    command = input()

    while command != 'END':
        r, c = map(int, command.split()[1:])  # skip the pointless 'Shoot'
        commands_list.append([r, c])
        command = input()
    return commands_list


def shoot_coord(player, row, col):
    if player[row][col] == '0':
        player[row][col] = 'x'
        return 'Missed'

    elif player[row][col] == '1':
        player[row][col] = 'x'
        return 'Booom'
    else:
        return 'You already shot there!'


def count_survived_boats(player):
    total = 0
    for row in player:
        total += row.count('1')
    return total


# приравнявам ред и колона към инт
rows, cols = map(int, input().split())

# чете дъската на играч 1
player_1 = read_player_board(rows)

# чете дъската на играч 2
player_2 = read_player_board(rows)

# прочита кординатите от инпута и маха shoot
coordinates = read_coordinates()

# проверява кой играч е на ред
player_1_turn = True

# преминавам през зададените координати за стрелба
# за всяка двойка координат от списъка:
for row, col in coordinates:

    # координатите на играч 1 са наобратно
    if player_1_turn:
        row, col = -row - 1, -col - 1  # Player two coords are reversed for no reason
        print(shoot_coord(player_2, row, col))
    else:
        print(shoot_coord(player_1, row, col))

    # прехвърля на следващия играч. това е съкратен вариант
    # иначе след всеки играч трябва да се пише T/F
    player_1_turn = not player_1_turn

# брой оцелелите кораби
p_1_result = count_survived_boats(player_1)
p_2_result = count_survived_boats(player_2)

print(f'{p_1_result}:{p_2_result}')
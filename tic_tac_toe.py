"""
    ---Tic Tac Toe---
    Rules:
    Player 1 : "X"
    Player 2 : "Y"
    Moves: 1 to 9
    Press "R" to reset game

"""

import subprocess, platform

def clr_shell():
    plat = platform.system()
    if plat == "Windows":
        subprocess.run('cls', shell=True)
    elif plat == "Linux":
        subprocess.run('clear', shell=True)



def mat_disp(lst):
    if [' ',' ',' '] in lst:
        cnt = 0
        for i in lst:
            if cnt!=2:
                print('', i[0], '||', i[1], '||', i[2])
                print("=============")
            else:
                print('', i[0], '||', i[1], '||', i[2])
            cnt+=1
    else:
        for i in lst:
            if i==lst[2]:
                print('', i[0], '||', i[1], '||', i[2])
            else:
                print('', i[0], '||', i[1], '||', i[2])
                print("=============")

def moves(lst, m, turn):
    place = {1: '0 0', 2: '0 1', 3: '0 2', 4: '1 0', 5: '1 1', 6: '1 2', 7: '2 0', 8: '2 1', 9: '2 2'}
    i, j = map(int, place[m].split(' '))
    if lst[i][j] == ' ':
        lst[i][j] = turn
    return lst

def check(x_lst, o_lst):
    draw = [1,2,3,4,5,6,7,8,9]
    lst = x_lst + o_lst
    lst.sort()
    win_list = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in win_list:
        flag_x = True
        flag_o = True
        for j in i:
            if j not in x_lst:
                flag_x = False
                break
        for j in i:
            if j not in o_lst:
                flag_o = False
                break
        if flag_o == True:
            return 'O'
        if flag_x == True:
            return 'X'
    if lst == draw:
        return "Draw"

def inp(turn, lst):
    l = [1,2,3,4,5,6,7,8,9]
    while True:
        print(str(turn)+"'s move:")
        i = input()
        try:
            if i == 'R' or i =='r':
                return i
            elif int(i) in l:
                return int(i)
        except:
            clr_shell()
            mat_disp(lst)
            print("Wrong Move!")

def game():
    x_list = []
    o_list = []
    XO_list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    count = 0
    while True:
        count+=1
        if count%2==1:
            turn = 'X'
            clr_shell()
            mat_disp(XO_list)
            move = inp(turn, XO_list)
            if move == 'R' or move == 'r':
                return 'R'
            XO_list = moves(XO_list, move, turn)
            x_list.append(move)
            x_list.sort()
        if count%2==0:
            turn = 'O'
            clr_shell()
            mat_disp(XO_list)
            move = inp(turn, XO_list)
            if move == 'R' or move == 'r':
                return 'R'
            XO_list = moves(XO_list, move, turn)
            o_list.append(move)
            o_list.sort()
        clr_shell()
        mat_disp(XO_list)
        result = check(x_list, o_list)
        if result == 'Draw':
            print("Match Draw!")
            print("Do you want to play again:(Y/N)")
            i = input()
            if (i=='y' or i=='Y' or i=='yes' or i=='Yes' or i=="YES"):
                return 'R'
            return 0
        if result == 'X' or result == 'O':      
            print(result, "is the winner!")
            print("Do you want to play again:(Y/N)")
            i = input()
            if (i=='y' or i=='Y' or i=='yes' or i=='Yes' or i=="YES"):
                return 'R'
            return 0
while True:
    clr_shell()
    print('''
            ---Tic Tac Toe---
    
    Rules:
    Player 1 : "X"
    Player 2 : "O"
    Moves: 1 to 9
    Press "R" to reset game
 
    Press Enter To Start!

    ''')
    input()
    clr_shell()
    i = game()
    if i !='R':
        exit()
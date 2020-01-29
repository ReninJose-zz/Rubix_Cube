import random
import sys 
from colored import fg, bg, attr

def instruction():
    print("")
    print("Color Codes:")
    print("W - White, B - Blue, G - Green, R - Red, O - Orange, Y - Yellow")
    print("Available Moves:") 
    print("TR - Moves top row to right side")
    print("TL - Moves top row to left side")
    print("BR - Moves bottom row to right side")
    print("BL - Moves bottom row to left side")
    print("LU - Moves left column to upwards")
    print("RU - Moves right row to upwards")
    print("LD - Moves left row to downwards")
    print("RD - Moves right row to downwards")
    go_back = 'y' 
    while go_back != 'y' or go_back != 'n':
        print("Do you want to go back to menu? If no, the game will exit. [y/n] ")
        go_back = input()
        if go_back == 'y':
            return menu()
        elif go_back == 'n':
            return sys.exit()
        if go_back != 'y' or go_back != 'n':
            print("Invalid command '{}'. Please try again".format(go_back))

def menu():
    help_command = 'start'
    while help_command != 'help' or help_command != 'start' or help_command != 'quit':
        print("")
        print("To start the game, type 'start'")
        print("For instructions on how to play this game type 'help'")
        print("To quit the game, type 'quit'")
        help_command = input()
        if help_command == 'help':
            instruction()
        if help_command == 'start':
            return
        if help_command == 'quit':
            return sys.exit()
        if help_command != 'help' or help_command != 'start' or help_command != 'quit':
            print("Invalid command '{}'. Please try again".format(help_command))

def coloring(lists):
    color = ['r','r','r','r']
    for i in range(4):
        if lists[i] == "R":
            color[i] = fg('red')
            
        if lists[i] == 'B':
            color[i] = fg('blue')
            
        if lists[i] == 'G':
            color[i] = fg('green')
            
        if lists[i] == 'O':
            color[i] = fg('orange_3')
            
        if lists[i] == 'Y':
            color[i] = fg('yellow')
            
        if lists[i] == 'W':
            color[i] = fg('white')
    return color

def printing():
    color_top = coloring(top)
    color_bottom = coloring(bottom)
    color_rs = coloring(right_side)
    color_ls = coloring(left_side)
    color_front = coloring(front)
    color_back = coloring(back)
    
    print("               {}  {}".format(color_top[0]+top[0],color_top[1]+top[1]))
    print("               {}  {}".format(color_top[2]+top[2],color_top[3]+top[3]))
    print("")
    print("{}   {}          {}  {}          {}  {}          {}  {}".format(color_ls[0]+left_side[0],color_ls[1]+left_side[1],color_front[0]+front[0],color_front[1]+front[1],color_rs[0]+right_side[0],color_rs[1]+right_side[1],color_back[0]+back[0],color_back[1]+back[1]))
    print("{}   {}          {}  {}          {}  {}          {}  {}".format(color_ls[2]+left_side[2],color_ls[3]+left_side[3],color_front[2]+front[2],color_front[3]+front[3],color_rs[2]+right_side[2],color_rs[3]+right_side[3],color_back[2]+back[2],color_back[3]+back[3]))
    print("")
    print("               {}  {}".format(color_bottom[0]+bottom[0],color_bottom[1]+bottom[1]))
    print("               {}  {}".format(color_bottom[2]+bottom[2],color_bottom[3]+bottom[3]))
    print(attr('reset'))

print("WELCOME TO THE RUBIX CUBE GAME")
menu()

move = 'a'
temp =[0,0,0,0]

temp_arrange = ['R','R','R','R','Y','Y','Y','Y','B','B','B','B','G','G','G','G','W','W','W','W','O','O','O','O']
random.shuffle(temp_arrange)
front = temp_arrange[0:4]
left_side = temp_arrange[4:8]
right_side = temp_arrange[8:12]
back = temp_arrange[12:16]
top = temp_arrange[16:20]
bottom = temp_arrange[20:24]


while(move != 'q'):
    printing()
    print("Type your move (if you want to quit the game, type 'q')")
    move = input()

    if move == "tr":
        temp[0] = front[0]
        temp[1] = front[1]
        front[0] = left_side[0]
        front[1] = left_side[1]
        left_side[0] = back[0]
        left_side[1] = back[1]
        back[0] = right_side[0]
        back[1] = right_side[1]
        right_side[0] = temp[0]
        right_side[1] = temp[1]
        temp[0] = top[0]
        top[0] = top[2]
        top[2] = top[3]
        top[3] = top[1]
        top[1] = temp[0]


    elif move == "tl":    
        temp[0] = front[0]
        temp[1] = front[1]
        front[0] = right_side[0]
        front[1] = right_side[1]    
        right_side[0] = back[0]
        right_side[1] = back[1]
        back[0] = left_side[0]
        back[1] = left_side[1]
        left_side[0] = temp[0]
        left_side[1] = temp[1]
        temp[0] = top[0]
        top[0] = top[1]
        top[1] = top[3]
        top[3] = top[2]
        top[2] = temp[0]

    elif move == "br": 
        temp[2] = front[2]
        temp[3] = front[3]
        front[2] = left_side[2]
        front[3] = left_side[3]
        left_side[2] = back[2]
        left_side[3] = back[3]
        back[2] = right_side[2]
        back[3] = right_side[3]
        right_side[2] = temp[2]
        right_side[3] = temp[3]
        temp[0] = bottom[0]
        bottom[0] = bottom[2]
        bottom[2] = bottom[3]
        bottom[3] = bottom[1]
        bottom[1] = temp[0]

    elif move == "bl":  
        temp[2] = front[2]
        temp[3] = front[3]
        front[2] = right_side[2]
        front[3] = right_side[3]
        right_side[2] = back[2]
        right_side[3] = back[3]
        back[2] = left_side[2]
        back[3] = left_side[3]
        left_side[2] = temp[2]
        left_side[3] = temp[3]
        temp[0] = bottom[0]
        bottom[0] = bottom[1]
        bottom[1] = bottom[3]
        top[3] = bottom[2]
        bottom[2] = temp[0]

    elif move == "lu":
        temp[0] = front[0]
        temp[2] = front[2]
        front[0] = bottom[0]
        front[2] = bottom[2]
        bottom[0] = back[0]
        bottom[2] = back[2]
        back[0] = top[0]
        back[2] = top[2]
        top[0] = temp[0]
        top[2] = temp[2]
        temp[0] = left_side[0]
        left_side[0] = left_side[1]
        left_side[1] = left_side[3]
        left_side[3] = left_side[2]
        left_side[2] = temp[0]

    elif move == "ru":
        temp[1] = front[1]
        temp[3] = front[3]
        front[1] = bottom[1]
        front[3] = bottom[3]
        bottom[1] = back[1]
        bottom[3] = back[3]
        back[1] = top[1]
        back[3] = top[3]
        top[1] = temp[1]
        top[3] = temp[3]
        temp[0] = right_side[0]
        right_side[0] = right_side[2]
        right_side[2] = right_side[3]
        right_side[3] = right_side[1]
        right_side[1] = temp[0]

    elif move == "ld":
        temp[0] = front[0]
        temp[2] = front[2]
        front[0] = top[0]
        front[2] = top[2]
        top[0] = back[0]
        top[2] = back[2]
        back[0] = bottom[0]
        back[2] = bottom[2]
        bottom[0] = temp[0]
        bottom[2] = temp[2]
        temp[0] = left_side[0]
        left_side[0] = left_side[2]
        left_side[2] = left_side[3]
        left_side[3] = left_side[1]
        left_side[1] = temp[0]

    elif move == "rd":
        temp[1] = front[1]
        temp[3] = front[3]
        front[1] = top[1]
        front[3] = top[3]
        top[1] = back[1]
        top[3] = back[3]
        back[1] = bottom[1]
        back[3] = bottom[3]
        bottom[1] = temp[1]
        bottom[3] = temp[3]
        temp[0] = right_side[0]
        right_side[0] = right_side[1]
        right_side[1] = right_side[3]
        right_side[3] = right_side[2]
        right_side[2] = temp[0]
    



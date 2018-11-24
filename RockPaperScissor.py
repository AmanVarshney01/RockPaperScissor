import random
import getpass
from time import sleep
print
print "welcome to Rock Paper Scissor"
print
print "1 = Vs. Computer\n2 = Vs. player"
mode = (input("Which mode do you want to play: "))

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == 'paper':
        return 1
    elif name == 'scissor' and name == 'scissors':
        return 2

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissor"

# when player choses Vs. computer mode
if mode == 1:
    player_name = (raw_input("What's your name: "))
    score = 0
    comp_score = 0
    while True:
        play = (raw_input("Are You Ready?(y/n): "))
        if play == 'y' and 'Y':
            player_choice = (raw_input("what's your choice: "))
            while player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissor' and 'scissors':
                print "OOPS! there is some problem! Write your choice again!"
                player_choice = (raw_input("What's your choice: "))
            sleep(1)
            def rps(player_choice):
                print
                global score
                global comp_score
                print player_name + "'s Choice: " + player_choice
                player_number = name_to_number(player_choice)
                comp_number = random.randrange(3)
                comp_choice = number_to_name(comp_number)
                sleep(.5)
                print "Computer's Choice: " + comp_choice
                difference = (comp_number - player_number) % 3
                for load in range(1):
                    print "Loading",
                    for i in range(4):
                        sleep(.5)
                        print '.',
                    sleep(.5)
                    print '.'
                if difference == 1:
                    sleep(1.2)
                    print "Computer wins!"
                    comp_score += 1
                    print "Computer" + "'s Score: " + str(comp_score)
                    print player_name + "'s Score: " + str(score)
                    print
                elif difference == 2:
                    sleep(1.2)
                    print player_name + " wins!"
                    score += 1
                    print player_name + "'s Score: " + str(score)
                    print "Computer" + "'s Score: " + str(comp_score)
                    print
                elif difference == 0:
                    sleep(1.2)
                    print player_name + " and computer tie!"
                    print player_name + "'s Score: " + str(score)
                    print "Computer" + "'s Score: " + str(comp_score)
                    print
            rps(player_choice)
        else:
            print "Thanks for playing!"
            sleep(2)
            break
# when player choses Vs. player mode
elif mode == 2:
    player1_name = (raw_input("What's the first player name: "))
    player2_name = (raw_input("What's the second player name: "))
    sleep(.2)
    print "Type your choice and hit ENTER"
    score1 = 0
    score2 = 0
    for again in range(100):
        while True:
            play = (raw_input("Are You Ready?(y/n): "))
            if play == 'y' and 'Y':
                player1_choice = getpass.getpass("what's " + player1_name + " choice: ")
                sleep(.5)
            player2_choice = getpass.getpass("what's " + player2_name + " choice: ")
            while player1_choice and player2_choice != 'rock' and player1_choice and player2_choice != 'paper' and \
                player1_choice and player2_choice != 'scissor' and 'scissors':
                print "OOPS! there is some problem! Write your choice again!"
                player1_choice = getpass.getpass("what's " + player1_name + " choice: ")
                sleep(.5)
                player2_choice = getpass.getpass("what's " + player2_name + " choice: ")
            sleep(.8)
            def rps(player1_choice):
                print ""
                global score2
                global score1
                sleep(.3)
                print player1_name + "'s Choice: " + player1_choice
                player1_number = name_to_number(player1_choice)
                player2_number = name_to_number(player2_choice)
                sleep(.1)
                print player2_name + " Choice: " + player2_choice
                difference = (player2_number - player1_number) % 3
                print "Loading",
                for i in range(4):
                    sleep(.5)
                    print '.',
                sleep(.5)
                print '.'
                if difference == 1:
                    sleep(2)
                    print player2_name + " wins!"
                    print
                    score2 += 1
                    print player2_name + "'s Score: " + str(score2)
                    print player1_name + "'s Score: " + str(score1)
                    print
                elif difference == 2:
                    sleep(2)
                    print player1_name + " wins!"
                    print
                    score1 += 1
                    print player1_name + "'s Score: " + str(score1)
                    print player2_name + "'s Score: " + str(score2)
                    print
                elif difference == 0:
                    sleep(2)
                    print player1_name + " and " + player2_name + " tie!"
                    print ""
                    print player1_name + "'s Score: " + str(score1)
                    print player2_name + "'s Score: " + str(score2)
                    print
            rps(player1_choice)
        else:
            print "Thanks for playing"
            sleep(2)
else:
    print("You have typed an inappropriate answer!")
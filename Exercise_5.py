#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
#
# win = 01  12  20
# lost = 10  02  21
import random
def computer():
    return random.randint(0, 2)

list = ['Snake', 'Water', 'Gun']
choice = computer()

def game():
    print('Enter your choice\n \t1 for snake\n\t2 for water\n\t3 for gun\n')
    userinput = int(input('Enter your choice:'))
    print('Your choice :', list[userinput])
    print("Computer chose:", list[choice])

    print('you win') if userinput-choice == (-1 or 2) else print(
        'draw') if userinput == choice else print('computer win')

print('\t\tWelcome to the game\n\n')
round = int(input('Enter the rounds that you want to play\n'))
for i in range(round):
    print('\t\tround', i + 1)
    game()
    i+1
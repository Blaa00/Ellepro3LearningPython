# import random
# o=0
# p=0
# while o !=35:
#     p+=1
#     o = 0
#     i=random.randint(1, 10)
#     print("____________________________")
#     print(i)
#     while i != 1:
#         o+=1
#         print(i)
#         i=random.randint (1, 10)
# 
# print("It took: {} times".format(p))
#

import random

i=0
while True:
    i=random.randint (1, 100)
    if i == 52 or i == 32 or i == 75:
        print("----------------------------------------------")
        print("Player 1 won press (F5/↑+Enter) to play again")
        print("----------------------------------------------")
        break;
    elif i == 62 or i == 45 or i== 82:
        print("----------------------------------------------")
        print("Player 2 won press (F5/↑+Enter) to play again")
        print("----------------------------------------------")
        break;
    else:
        print("------------------------------------------------------------------------------------------------------------------")
        print("No boddy won the number was {} player 1 has 52, 32 and 75. player 2 has 62, 45 and 82. press (Enter) to play again".format(i))
        print("------------------------------------------------------------------------------------------------------------------")
    input("")

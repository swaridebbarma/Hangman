import random   
name=input("my name is ") 
print("welcome")
print("play game")
topic=["loop","list","file","json","function","dictonary"]
wrd=random.choice(topic)
print(wrd)
chns=8
guess=""
alphabet=("abcdefghijklmnopqrstuvwxyz")
while len(wrd)>0:
    mn_wrd= ""
    for letter in wrd:
        if letter in guess:
           mn_wrd= mn_wrd+letter
        else:
            mn_wrd=mn_wrd+"_ "
    if mn_wrd==wrd:
        print(mn_wrd)
        print(" congreatulation your guessed is correct")
        print("you are win")
        break
    print("guess the wrd",mn_wrd)
    guess1=input()
    if guess1 in alphabet:
        guess+=guess1
    else:
        print("enter valide charecter")
        guess=input()
    if guess not in wrd:
        chns=chns-1
        if chns==8:
                print("8 chns is left")
                print("-------")
                print("      o     ")   
        if chns==7:
                print("7 chns is left")
                print("---------")
                print("      o    ")
                print("      |    ")
        if chns==6:
                print("6 chns is left")
                print("---------")
                print("      o     ")
                print("      |     ")
                print("     /      ")
        if chns==5:
                print("5 chns is left")
                print("---------")
                print("      o     ")
                print("      |     ")
                print("     / \    ")
        if chns==3:
                print("3 chns is left")
                print("------------")
                print("     \o     ")
                print("      |     ")
                print("     / \    ")
        if chns==2:
                print("2 chns is left")
                print("------------")
                print("     \o/   | ")
                print("      |     ")
                print("     / \    ")
        if chns==1:
                print("1 chns is left")
                print("------------")
                print("     \o/ _| ")
                print("      |     ")
                print("     / \   ")
        if chns==0:
                print("0 chns is left")
                print("------------")
                print("      o_|   ")
                print("     /|\    ")
                print("     \/ \    ")
                print("you are loss")
                break
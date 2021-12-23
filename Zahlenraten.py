import random
#explanation to the comments:
#a * at the begin shows the following correlates to the comment before
#** for the foreleast comment.....
#a comment is always the explanation until the next one

result=[]
j=0

def Reset():#things that are only counted and are only guilty for one round; not clear if necessary
    blub=0#only that there ist no error for the next part

def end():
    again=input("Do you want to play again? [j/n] ")#ask for a new play, controls the input
    while again!="j" and again !="n":
        print('Please answer only with "j" or "n".')
        again=input("Do you want to play again? j/n")
    if again=="j":
        Reset()
        start()#begins from start again
    elif again=="n":
        exit()#ends program
    

def start():
    while True: #ask for an integer
        try:
            range1=int(input("Please choose a start: "))
            break
        except ValueError:
            print("The input have to be an integer!")
    while True: #aks for a different one, bigger then the first
        try:
            range2=int(input("Please choose an end: "))
            while range2<=range1:
                print("The end has to be greater then the start")
                range2=int(input("Please choose an end: "))
            break
        except ValueError:
            print("The input have to be an integer!")
    
    randomnumber=(random.randint(range1,range2)) #create a random integer, 
    while guess !=randomnumber:
        guessesperround=1
        while True: #ask for an guesses integer
            try:
                guess=int(input("Please guess an integer: "))
                break
            except ValueError:
                print("The input have to be an integer!")
        if guess<range1 or guess>range2:#*between the guessed numbers, if not, aks again
            print("The guesses intger has to be in the choosen range.")
        if guess < randomnumber:#gives a tip, where the integer is
            print("The random integer is greater then "+str(guess))
        elif guess >randomnumber:
            print("he random integer is smaller then "+str(guess))
        elif guess==randomnumber:#if guess is right...
            if guessesperround>1:
                print("You've done it in the "+str(guessesperround)+". try. : ) The random integer is "+str(randomnumber))
            else:
                print("You've done it in your first try. : ) The random integer is "+str(randomnumber))
            result[roundsplayd] = [guessesperround]#write it into a list for an highscore
            result.sort()#sort it from the smallest to the biggest
            roundsplayd=result.count()#get the number of rounds
            counterprint=0#define new integer for printing the highscore
            while counterprint<=roundsplayd:
                print(str(result[counterprint]))#print the highscore
                counterprint+=1#print the next result
            end()
        guessesperround+=1#counts the guesses for the highscore

start()





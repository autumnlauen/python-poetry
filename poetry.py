"""
File: poetry.py
Author: Autumn Lauen
Description: A program that takes in a poem/poems and changes it.
"""

def nPlus(poem,number):
    inputNouns=open("nounlist.txt","r")
    nounList=[]
    for line in inputNouns:
        line=line[0:-1]
        nounList.append(line)
    inputNouns.close()

    inputPoem=open(poem,'r')
    newPoemName="nPlus_"+poem
    outputPoem=open(newPoemName,'w')
    masterList=[]
    for line in inputPoem:
        original=line
        line=line.replace(".","")
        line=line.replace(",","")
        line=line.replace("!","")
        line=line.replace("?","")
        line=line.replace(";","")
        line=line.replace("(","")
        line=line.replace(")","")
        line=line.replace("{","")
        line=line.replace("}","")
        line=line.replace(":","")
        line=line.replace("-"," ")
        line=line.lower()
        line=line.split()
        for word in line:
            if word in nounList:
                position=nounList.index(word)
                newPosition=(position+number)%len(nounList)
                newWord=nounList[newPosition]
                original=original.replace(word,newWord)
        masterList.append(original)
    inputPoem.close()
    for line in masterList:
        outputPoem.write(line)
    outputPoem.close()

    print("Finished!")
    print()
    print(newPoemName,"has been saved in your folder.")
                
    return None


def centoGenerator(letters,lines):
    import random

    masterList=[]

    for letter in letters:
        if letter=="a":
            dickinson=open("ifishoulddie.txt","r")
            for line in dickinson:
                masterList.append(line)
            dickinson.close()
        elif letter=="b":
            angelou=open("cagedbird.txt","r")
            for line in angelou:
                masterList.append(line)
            angelou.close()
        elif letter=="c":
            whitman=open("ohcaptainmycaptain.txt","r")
            for line in whitman:
                masterList.append(line)
            whitman.close()
        elif letter=="d":
            hughes=open("itoo.txt","r")
            for line in hughes:
                masterList.append(line)
            hughes.close()
        elif letter=="e":
            poe=open("theraven.txt","r")
            for line in poe:
                masterList.append(line)
            poe.close()
        elif letter=="f":
            frost=open("theroadnottaken.txt","r")
            for line in frost:
                masterList.append(line)
            frost.close()
        elif letter=="g":
            lowell=open("venustransiens.txt","r")
            for line in lowell:
                masterList.append(line)
            lowell.close()

    cento=open("cento.txt","w")

    indexList=[]

    count=0
    for line in masterList:
        indexList.append(count)
        count+=1

    for line in range(lines):
        index=random.choice(indexList)
        cento.write(masterList[index])

    cento.close()

    print("Finished!")
    print()
    print("cento.txt has been saved in your folder.")    

    return None

def blackoutGenerator(poem,words):
    import random
    
    inputPoem=open(poem,'r')
    newPoemName="blackout_"+poem
    outputPoem=open(newPoemName,'w')

    wordList=[]

    for line in inputPoem:
        line=line.replace(".","")
        line=line.replace(",","")
        line=line.replace("!","")
        line=line.replace("?","")
        line=line.replace(";","")
        line=line.replace("(","")
        line=line.replace(")","")
        line=line.replace("{","")
        line=line.replace("}","")
        line=line.replace(":","")
        line=line.replace("-"," ")
        line=line.lower()
        line=line.split()
        for word in line:
            wordList.append(word)            

    inputPoem.close()

    indexList=[]
    count=0
    for line in wordList:
        indexList.append(count)
        count+=1
        
    if words<=0:
        print("That is not a valid amount of words.")
        return None
    else:
        for line in range(words):
            index=random.choice(indexList)
            outputPoem.write(wordList[index])
            outputPoem.write("\n")

    outputPoem.close()

    print("Finished!")
    print()
    print(newPoemName,"has been saved in your folder.")

    return None

def main():
    chosenMod="~"
    chosenLetter="~"
    lettersChosen="~"
    linesChosen="~"
    chosenNum="~"
    chosenLet="~"
    end="~"
    while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
        print("Welcome!")
        print()
        print("How would you like to modify poems?")
        print()
        print("1) Change nouns using the nPlus method")
        print("2) Create a new cento poem using lines from multiple poems")
        print("3) Create a blackout poem using random words from your selected poem")
        print()
        chosenMod=input("Type the number of the modification you would like to perform: ")
        while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
            print()
            print("------------------------------------------")
            print()
            if chosenMod=="1":
                print("You have chosen the nPlus modification!")
                print()
                print("Which poem would you like to modify?")
                print()
                print("a) If I should die by Emily Dickinson")
                print("b) Caged Bird by Maya Angelou")
                print("c) Oh Captain! My Captain! by Walt Whitman")
                print("d) I, too by Langston Hughes")
                print("e) The Raven by Edgar Allan Poe")
                print("f) The Road Not Taken by Robert Frost")
                print("g) Venus Transiens by Amy Lowell")
                print()
                chosenLet=(input("Type the letter of the poem you would like to modify: "))
                while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
                    print()
                    letterList=["a","b","c","d","e","f","g"]
                    if chosenLet not in letterList:
                        print("That letter is not one of the available choices. Try again or enter q to quit.")
                        print()
                        chosenLet=(input("Type the letter of the poem you would like to modify: "))
                    else:
                        print()
                        print("------------------------------------------")
                        print()
                        print("How many words down in the noun list would you like to change the nouns to?")
                        print()
                        chosenNum=input("Type a number here: ")
                        while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
                            print()
                            for character in chosenNum:
                                if 0<=ord(character)<=47 or 58<=ord(character)<=127:
                                    print("That is not a valid number for this function. Try again or enter q to quit.")
                                    print()
                                    chosenNum=input("Type a number here: ") 
                            print()
                            print("------------------------------------------")
                            print()
                            if chosenLet=="a":
                                nPlus("ifishoulddie.txt",int(chosenNum))
                            elif chosenLet=="b":
                                nPlus("cagedbird.txt",int(chosenNum))
                            elif chosenLet=="c":
                                nPlus("ohcaptainmycaptain.txt",int(chosenNum))
                            elif chosenLet=="d":
                                nPlus("itoo.txt",int(chosenNum))
                            elif chosenLet=="e":
                                nPlus("theraven.txt",int(chosenNum))
                            elif chosenLet=="f":
                                nPlus("theroadnottaken.txt",int(chosenNum))
                            elif chosenLet=="g":
                                nPlus("venustransiens.txt",int(chosenNum))
                            end="q"
                                

            elif chosenMod=="2":
                print("You have chosen the cento modification!")
                print()
                print("Which poems would you like to include?")
                print()
                print("a) If I should die by Emily Dickinson")
                print("b) Caged Bird by Maya Angelou")
                print("c) Oh Captain! My Captain! by Walt Whitman")
                print("d) I, too by Langston Hughes")
                print("e) The Raven by Edgar Allan Poe")
                print("f) The Road Not Taken by Robert Frost")
                print("g) Venus Transiens by Amy Lowell")
                print()
                lettersChosen=input("Type the letters of the poems you want to include. For example, abc: ")
                while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
                    print()
                    letterList=["a","b","c","d","e","f","g"]
                    letterSet=set()
                    for letter in letterList:
                        letterSet.add(letter)
                    chosenSet=set()
                    for letter in lettersChosen:
                        chosenSet.add(letter)
                    different=chosenSet.difference(letterSet)
                    if len(different)!=0:
                        print("One or more of those letters is not a valid entry. Try again or enter q to quit.")
                        print()
                        lettersChosen=input("Type the letters of the poems you want to include. For example, abc: ")
                    else:
                        print("------------------------------------------")
                        print()
                        print("How many lines would you like in your cento poem?")
                        print()
                        linesChosen=input("Type a number here: ")
                        while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
                            print()
                            for character in linesChosen:
                                if 0<=ord(character)<=47 or 58<=ord(character)<=127:
                                    print("That is not a valid number for this function. Try again or enter q to quit.")
                                    print()
                                    linesChosen=input("Type a number here: ")
                            if int(linesChosen)<=0:
                                print("That is not a valid number for this function. Try again or enter q to quit.")
                                print()
                                linesChosen=input("Type a number here: ")
                            print()
                            print("------------------------------------------")
                            print()
                            centoGenerator(lettersChosen,int(linesChosen))
                            end="q"
                                
            elif chosenMod=="3":
                print("You have chosen the blackout modification!")
                print()
                print("Which poem would you like to modify?")
                print()
                print("a) If I should die by Emily Dickinson")
                print("b) Caged Bird by Maya Angelou")
                print("c) Oh Captain! My Captain! by Walt Whitman")
                print("d) I, too by Langston Hughes")
                print("e) The Raven by Edgar Allan Poe")
                print("f) The Road Not Taken by Robert Frost")
                print("g) Venus Transiens by Amy Lowell")
                print()
                chosenLetter=(input("Type the letter of the poem you would like to modify: "))
                while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
                    letterList=["a","b","c","d","e","f","g"]
                    if chosenLetter not in letterList:
                        print()
                        print("That letter is not one of the available choices. Try again or enter q to quit.")
                        print()
                        chosenLetter=(input("Type the letter of the poem you would like to modify: "))
                    else:
                        print()
                        print("------------------------------------------")
                        print()
                        print("How many words would you like in your blackout poem?")
                        print()
                        chosenNum=input("Type a number here: ")
                        while chosenMod!="q" and chosenLetter!="q" and lettersChosen!="q" and linesChosen!="q" and chosenNum!="q" and chosenLet!="q" and end!="q":
                            print()
                            for character in chosenNum:
                                if 0<=ord(character)<=47 or 58<=ord(character)<=127:
                                    print("That is not a valid number for this function. Try again or enter q to quit.")
                                    print()
                                    chosenNum=input("Type a number here: ") 
                            print()
                            print("------------------------------------------")
                            print()
                            if chosenLetter=="a":
                                blackoutGenerator("ifishoulddie.txt",int(chosenNum))
                            elif chosenLetter=="b":
                                blackoutGenerator("cagedbird.txt",int(chosenNum))
                            elif chosenLetter=="c":
                                blackoutGenerator("ohcaptainmycaptain.txt",int(chosenNum))
                            elif chosenLetter=="d":
                                blackoutGenerator("itoo.txt",int(chosenNum))
                            elif chosenLetter=="e":
                                blackoutGenerator("theraven.txt",int(chosenNum))
                            elif chosenLetter=="f":
                                blackoutGenerator("theroadnottaken.txt",int(chosenNum))
                            elif chosenLetter=="g":
                                blackoutGenerator("venustransiens.txt",int(chosenNum))
                            end="q"
                            
            else:
                print("That is not one of the available choices. Try again or enter q to quit.")
                print()
                chosenMod=input("Type the number of the modification you would like to perform: ")
    print()
    print("Thank you! Have a great day!")
    print()
    input("Press enter to quit.")
main()

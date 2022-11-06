from random import choice
words=["curtain", "chair", "clothes", "shirt", "pantyhose","kitchen","cave","shelf","skirt","drawer","cupboard","soup","lego","tiger","train","python","bag","bug","pants","mouse","owl","star","phone"]
#select a random word:
#it returns display
def select_word(words):
    global random_word
    global display
    display = "_"
    random_word = choice(words)
    display = len(random_word)*"_"
    display = list(display)
    return display
#it checks the output:
def validate(input):
    if len(letter) > 1:
        print("Invalid input!")
#it checks the letter is correct or not, and add it to the right list and display it:
def checking_letter(letter):
    display1=list(display)
    indexnum=0
    if letter in random_word:
        for i in random_word:
            if i == letter:
                indexnum=random_word.index(i)
                display[indexnum]=i
                return display

    else:
        global lives
        lives-=1
        wrong_letters.append(letter)
        print(f"Wrong letters:{wrong_letters}")
        print(f"Remaining lives:{lives}")
        return lives
#Won or not:
#it displays if you lost or won:
def won_lost():
    if lives == 0:
        print('\n' + '!' * 20 + '\n')
        print(f"You have been hanged!Ha-ha-ha!! The word was {random_word}.")
        print('\n' + '!' * 20 + '\n')
        quit()
    elif '_' not in display:
        print('\n' + '*' * 20 + '\n')
        print(f"Congratulations, you have won!! You even have {lives} lives left!")
        print('\n' + '*' * 20 + '\n')
        quit()

#The game:
lives=6
wrong_letters=[]
select_word(words)
print('\n'+'*'*20+'\n')
print(select_word(words))
print('\n'+'*'*20+'\n')
while lives > 0 :
    letter=str(input("Please, write a letter: "))
    validate(letter)
    checking_letter(letter)
    print(display)
    won_lost()











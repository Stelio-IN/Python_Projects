
#_______________________________
def new_game():
    guesses = []
    correct_gesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C or D): ").upper()
        guesses.append(guess)

        correct_gesses += check_answer(questions.get(key),guess)
        question_num+=1

    display_score(correct_gesses,guesses)

#_______________________________
def check_answer(aswer, guess):

    if aswer == guess:
        print("Correct! :)")
        return 1
    else:
        print("Wrong! :(")
        return 0
#_______________________________
def display_score(correct_guesses,guesses):
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    print("Answers: ", end= "")
    for i in questions:
        print(questions.get(i),end =" ")
    print()

    print("Guesses: " , end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = ((correct_guesses/len(questions))*100)
    print("your score is: "+ str(score)+"%")
#_______________________________
def play_again():
    response = input("Do you want to play again? (yes or no):").upper()
    if response == "YES":
        return True
    else:
        return False
#_______________________________

questions = {
    "Who created pyton?: ":"A",
    "What year was python created?: ": "B",
    "Who was the first president in Moz?: ": "C",
    "what is the Better University in MOZ?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Joaquim Chissano", "B. Armando guebuza", "C. Samara Machel", "D. Eduardo Mondlane"],
           ["A. UEM", "B. UP", "C. UJC", "D. ISUTC"],
]

#rodar antes de entrar no loop
new_game()
while play_again():
    new_game()
print("Exiting")
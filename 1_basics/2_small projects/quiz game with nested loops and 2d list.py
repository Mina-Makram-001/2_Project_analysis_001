#quiz game with nested loops and 2d lists

questions=("what is the biggest planet : ",               #normal list
           "which degree the water boils at : ",
           "what is the biggest animal : ")

options=(("a. the earth ", "b. the sun ", "c. mercury "), #2d list
         ("a. 90C ", "b. 100C ", "c. 110C "),
         ("a. cat ", "b. dog ", "c. donkey "))

guesses=[]
answers=("a", "b", "c")

score=0
questions_num=0

for question in questions:
    print("--------------------")
    print(question)
    
    for option in options[questions_num]:
        print(option)

    guess=input("inter your answer (a, b, c) : ").lower()
    guesses.append(guess)
    
    if guess==answers[questions_num]:
        print("your answer is correct ! ")
        score+=1
        
    
    else:
        print("answer is wrong !! ")
        print(f"answer {answers[questions_num]} is the correct answer")
    
    questions_num+=1  

print("--------------------")
print("      answers       ")
print("--------------------")

for answer in answers[questions_num]:
    print(answer, end=" ")
print()

for guess in guesses[questions_num]:
    print(guess, end=" ")
print()

yourscore=(score/questions_num)*100

print(f"your score is {yourscore}")















    
    

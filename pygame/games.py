"""
import random

words = ["python", "developer", "coding", "challenge"]
word = random.choice(words)
guessed = ["_" for _ in word]
attempts = 6

while attempts > 0 and "_" in guessed:
   print("Word: ", " ".join(guessed))
   guess = input("Guess a letter: ")
   if guess in word:
       for i in range(len(word)):
           if word[i] == guess:
               guessed[i] = guess
   else:
       attempts -= 1
       print(f"Incorrect! {attempts} attempts left.")
   
if "_" not in guessed:
   print("Congrats! You found the word:", word)
else:
   print("Game over! The word was:", word)
   """

""" questions = {
   "What is the capital of France?": "Paris",
   "Which planet is known as the Red Planet?": "Mars",
   "What is 5 + 3?": "8"
}

score = 0

for question, answer in questions.items():
   user_answer = input(question + " ").strip().capitalize()
   if user_answer == answer:
       print("Correct!")
       score += 1
   else:
       print(f"Wrong The correct answer is {answer}.")

print(f"Final Score: {score}/{len(questions)}") """

""" import random

def scramble_word(word):
   return "".join(random.sample(word, len(word)))

words = ["python", "developer", "programming", "challenge"]
word = random.choice(words)
scrambled = scramble_word(word)

print("Scrambled word:", scrambled)

attempts = 3
while attempts > 0:
   guess = input("Guess the word: ").lower()
   if guess == word:
       print("Correct! ????")
       break
   else:
       attempts -= 1
       print(f"Wrong! {attempts} attempts left.")

if attempts == 0:
   print(f"Game over! The correct word was {word}.")

print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you follow any author on AskPython? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of your favourite website for learning Python?')
    if answer.lower()=='askpython':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!') """

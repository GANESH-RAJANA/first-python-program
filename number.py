#GET GUESS
import random
def get_guess():
    return list(input("What is your guess"))

#GENERATE COMPUTER CODE123

def generate_code():
    digits = [str(num) for num in range(10)]

    #suffle the digits
    random.shuffle(digits)

    #then grab the first three
    return digits[:3]

# GENERATE CLUES

def generate_clues(code,user_guess):

    if user_guess==code:
        return "CODE IS CRACKED"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num == code:
            clues.append("Close")

    if clues == []:
        return ["nope"]
    else:
        return clues

#RUN GAME LOGIC

print("welcome Code Braker!")
secret_code = generate_code()
clue_report = []
while clue_report != "CODE IS CRACKED":
      guess = get_guess()

      clue_report = generate_clues(guess,secret_code)
      print("Here is result of your guess:")
      for clues in clue_report:
          print(clues)

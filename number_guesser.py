import random

'''
number guessing game >> picks a random number , user has to guess it, program gives hints (cold/ hot), based on how far or clsoe the user guess was.
'''
class NumberGuesser:
    def __init__(self):
        print('##########################')
        print('     Number Guesser')
        print('##########################')
        
        self.tries = 0
        self.number = random.randint(1, 10)

    def start_game(self):
        while(True):
            try:
                answer = int(input('enter your guess: '))
                if answer not in range(1,11):
                    raise ValueError(f"number not in the range of (1,10)")


                if answer == self.number:
                    self.tries += 1
                    print("correct guess!!")
                    print(f"you completed this challenge in {self.tries} attempts!!")
                    break
                else:
                    gap = abs(answer-self.number)
                    if gap > 5:
                        print('hint: cold')
                    elif gap <= 2:
                        print('hint: hot')
                    elif gap <= 5:
                        print('hint: warm')
                    print("gg")
                    self.tries += 1

            except ValueError as e:
                print(f"error: {e}")
                print(f"please enter a int value between (1,10)")



game = NumberGuesser()
game.start_game()

from .die import Die

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def refresh(self):
         self.dice = Die.create_dice(5)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):

        # Probably counts wins or something.
        # Great variable name, 10/10.

        # number of wins in the row
        c = 0

        # Define it globally to keep track of losses and wins
        runner = cls()

        while True:

            # generate a new combination of the dice
            runner.refresh()

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                c += 1
                runner.wins = c
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                
                runner.loses +=1
                c = 0
                runner.wins = 0

            print("Wins: {} Loses {}".format(runner.wins, runner.loses))

            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break
            
            prompt = input("Would you like to play again?[Y/n]: ") 
            
            if prompt not in ['Y', 'n', '']:

                while prompt not in ['Y', 'n', '']:
                    prompt = input('Please type "n" for no or "Y" for yes: ')

            if prompt == 'Y' or prompt == '':
                continue

            else:
                break

        
                #i_just_throw_an_exception()
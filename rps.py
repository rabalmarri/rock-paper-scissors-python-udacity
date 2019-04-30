import random
import time
import sys


the_moves = ['rock', 'paper', 'scissors']


class rockyman:

    def __init__(self):
        """Initialize a Player instance."""
        self.score = 0

    def move(self):
        """Return the move and her always rock."""
        return 'rock'

    def learn(self, last_opponent_move):
        """
        Allow subclasses to save the move made by the opponent on the
        last round. This her is empty because this class doesn't
        use this information.
        """
        pass


class RandomBOY(rockyman):
    """RandomBOY class: chooses its move at random."""

    def move(self):
        """Return the  move in a random."""
        his_move = random.randint(0, 2)
        return the_moves[his_move]


class mirrorBOY (rockyman):
    """
        mirrorBOY class: remembers what move you play last
        round, and play it this round.
    """

    def __init__(self):
        """Initialize a mirrorBOY instance."""
        rockyman.__init__(self)
        self.last_op_move = None

    def move(self):
        """Return last opponent move."""
        if self.last_op_move is None:
            return rockyman.move(self)
        else:
            return self.last_op_move

    def learn(self, last_op_move):
        """Save the move made by the opponent on the last round.
        Args:
            last_op_move (string): Opponent's move on the last round.
        """
        self.last_op_move = last_op_move


class circularBoy(rockyman):
    """
        circularBoy class: remembers his move last round, and
        cycles through the diferent moves.
    """

    def __init__(self):
        """Initialize a circularBoy instance."""
        rockyman.__init__(self)
        self.last_move = None

    def move(self):
        """Return the move in a cycles."""
        move = None
        if self.last_move is None:
            move = rockyman.move(self)
        else:
            index = the_moves.index(self.last_move) + 1
            if index >= len(the_moves):
                index = 0
            move = the_moves[index]
        self.last_move = move
        return move


class yourPlay(rockyman):
    def move(self):
        """yourPlay class: ask the user to input the move."""
        while True:
            time.sleep(0.5)
            player_move = input("Enter your move\n"
                                "1. rock\n"
                                "2. paper\n"
                                "3. scissors\n")
            if player_move == '1':
                return the_moves[0]

            elif player_move == '2':
                return the_moves[1]

            elif player_move == '3':
                return the_moves[2]

            else:
                print('what??\n')
                yourPlay.move


class Game():
    """
    Game class: Play a match of Rock, Paper or Scissor.
    the first one take 3 as his score win
    """

    def __init__(self):
        """Initialize a Game instance."""
        self.you = yourPlay()
        self.opposite = rockyman()

    def play_match(self):
        """
        start the game by display a welcome message at the beggining and
        choseing you opposite player and play match of 3 score
        and printing the score
        """
        time.sleep(1)
        print("Let's play Rock, Paper or Scissors!\n")
        while True:
            self.plyer_op()
            while self.you.score != 3 or self.opposite.score != 3:

                self.play_round()
                print('your score :' + str(self.you.score) + ' vs ' +
                      "the opposite player :" +
                      str(self.opposite.score) + '\n')
                if self.you.score == 3:
                    print("you win!! the match\n")
                    break
                elif self.opposite.score == 3:
                    print("opposite player win!! the match\n")
                    break
            self.you.score = 0
            self.opposite.score = 0

    def play_round(self):
        """
        her it is singel round with printing your scor and the opposite pleyer
        and give you how win

        Returns:


        if 1 you won, if 2 opposite won or if 0 it is draw.
        """
        your_move = self.you.move()
        opposite_move = self.opposite.move()
        result = Game.what_move(your_move, opposite_move)

        self.you.learn(opposite_move)
        self.opposite.learn(your_move)

        print("you choose:" + your_move + " and the opposite player choose:" +
              opposite_move)

        if result == 1:
            self.you.score += 1
            print('=> you won this round!\n')
        elif result == 2:
            self.opposite.score += 1
            print('=> the opposite pleyer won this round!\n')
        elif result == 0:
            print('=> it is Draw!\n')

    @classmethod
    def what_move(cls, your_move, opposite_move):
        """her sitting the rules of the game """
        if your_move == opposite_move:
            return 0

        elif your_move == 'rock' and opposite_move == 'scissors':
            return 1

        elif your_move == 'rock' and opposite_move == 'paper':
            return 2

        elif your_move == 'paper' and opposite_move == 'rock':
            return 1

        elif your_move == 'paper' and opposite_move == 'scissors':
            return 2

        elif your_move == 'scissors' and opposite_move == 'paper':
            return 1

        elif your_move == "scissors" and opposite_move == 'rock':
            return 2

    def plyer_op(self):
        """her you chose you opposite plyer"""
        time.sleep(1)
        while True:
            choice = input("how do you wint play with??\n"
                           "1. rockyman\n"
                           "2. RandomBOY\n"
                           "3. mirrorBOY\n"
                           "4. circularBoy\n"
                           "5. leave\n ")
            if choice == '1':
                self.opposite = rockyman()
                break
            elif choice == '2':
                self.opposite = RandomBOY()
                break
            elif choice == '3':
                self.opposite = mirrorBOY()
                break
            elif choice == '4':
                self.opposite = circularBoy()
                break
            elif choice == '5':
                sys.exit("Bye")
                break
            else:
                print('what??\n')
                Game.plyer_op


game = Game()
game.play_match()

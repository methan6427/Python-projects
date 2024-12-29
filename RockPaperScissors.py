

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("Rock, Paper, or Scissors? ").strip().lower()
            if choice in moves:
                return choice
            print("Invalid move. Please try again.")


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = None

    def move(self):
        return self.their_last_move\
            if self.their_last_move\
            else random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = None

    def move(self):
        if not self.my_last_move:
            self.my_last_move = 'rock'
        else:
            self.my_last_move = (
                moves)[(moves.index(self.my_last_move) + 1)
                       % len(moves)]
        return self.my_last_move

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


def beats(one, two):
    return (
        (one == 'rock' and two == 'scissors') or
        (one == 'scissors' and two == 'paper') or
        (one == 'paper' and two == 'rock')
    )


class Game:
    def __init__(self, p1, p2, rounds=3):
        self.p1 = p1
        self.p2 = p2
        self.rounds = rounds
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, round_num):
        print(f"Round {round_num + 1}:")
        print(f"Player 1 Score: {self.p1_score}")
        print(f"Player 2 Score: {self.p2_score}")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("Game Tied!")
        elif beats(move1, move2):
            print("Player 1 Wins the round!")
            self.p1_score += 1
        else:
            print("Player 2 Wins the round!")
            self.p2_score += 1

        print(f"Current scores:"
              f"\nPlayer 1: {self.p1_score}  "
              f"Player 2: {self.p2_score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round_num in range(self.rounds):
            self.play_round(round_num)
        print("Game over!")
        print("Final scores:")
        print(f"Player 1: {self.p1_score}\nPlayer 2: {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("Player 1 Wins the game!")
        elif self.p1_score < self.p2_score:
            print("Player 2 Wins the game!")
        else:
            print("No winner! It's a draw!")


if __name__ == '__main__':
    print("Welcome to Rock Paper Scissors!")
    while True:
        print("Lets play Rock Paper Scissors!")
        print("Type Starter, Easy, Medium, or Hard to Begin!")
        print("Type Exit to quit")
        mode = input("Please select a game mode: ").strip().lower()
        if mode == "starter":
            print("Starter Mode Selected")
            game = Game(AllRockPlayer(), AllRockPlayer(), rounds=3)
            game.play_game()
        elif mode == "easy":
            print("Easy Mode Selected")
            game = Game(HumanPlayer(), RandomPlayer(), rounds=3)
            game.play_game()
        elif mode == "medium":
            print("Medium Mode Selected")
            game = Game(HumanPlayer(), ReflectPlayer(), rounds=5)
            game.play_game()
        elif mode == "hard":
            print("Hard Mode Selected")
            game = Game(HumanPlayer(), CyclePlayer(), rounds=7)
            game.play_game()
        elif mode == "exit":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid mode. Please try again.")

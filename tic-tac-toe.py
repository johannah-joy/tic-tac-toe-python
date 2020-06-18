
class Player():

  def __init__(self, name, token):
    # name = input("Player Name:")
    self.name = name
    # token = X or O
    self.token = token

class Game():

  def __init__(self):
    self.square = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

  def __repr__(self):
    print(f"{self.square[1]} | {self.square[2]} | {self.square[3]}")
    print(f"{self.square[4]} | {self.square[5]} | {self.square[6]}")
    print(f"{self.square[7]} | {self.square[8]} | {self.square[9]}")

  # update board after each turn
  def update_square(self, square_num, player):
    if self.square[square_num] == " ":   # players can only go in an empty square
      self.square[square_num] = player

  def calc_winner(self, player):
    if self.square[1] == player and self.square[2] == player and self.square[3] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[4] == player and self.square[5] == player and self.square[6] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[7] == player and self.square[8] == player and self.square[9] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[1] == player and self.square[4] == player and self.square[7] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[2] == player and self.square[5] == player and self.square[8] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[9] == player and self.square[6] == player and self.square[3] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[7] == player and self.square[5] == player and self.square[3] == player:
      print(f"Player {player} won!")
      return True
    elif self.square[1] == player and self.square[5] == player and self.square[9] == player:
      print(f"Player {player} won!")
      return True
    else:
      return False

  def tie(self):
    unavailable_squares = 0
    for square in self.square:
      if square != " ":
        unavailable_squares += 1
    if unavailable_squares == 9:
      return True
    else:
      return False
  
  def is_game_over(self):
    return self.tie() or self.calc_winner()


game = Game()
# display board
game.__repr__()

while True:
  player_x_choice = int(input("Player X, what square number would you like to place your token? (1-9) "))
  # update board
  game.update_square(player_x_choice, "X")
  print(game.__repr__())
  # checking for a win for player X
  if game.calc_winner("X") == True:
    print("Player X is the winner!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
      game.__init__()
      print(game.__repr__())
      continue
    else:
      break
  # checking for a tie, after Player X goes
  if game.tie() == True:
    print("The board is full. It's a TIE!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
      game.__init__()
      print(game.__repr__())
      continue
    else:
      break
  player_o_choice = int(input("Player O, what square number would you like to place your token? (1-9) "))
  # update board
  game.update_square(player_o_choice, "O")
  print(game.__repr__())
  # checking for a win for player O
  if game.calc_winner("O") == True:
    print("Player O is the winner!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
      game.__init__()
      print(game.__repr__())
      continue
    else:
      break
  # checking for a tie, after Player O goes
  if game.tie() == True:
    print("The board is full. It's a TIE!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
      game.__init__()
      print(game.__repr__())
      continue
    else:
      break
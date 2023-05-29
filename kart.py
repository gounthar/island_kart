from items import Coin, Shell, Heart, Bomb
import emoji 

class Kart:
  def __init__(self, start_pos, row_idx):
    self.char = '8'
    self.char = emoji.emojize(':oncoming_automobile:')
    self.coins = 0
    self.health = 100
    self.pos = start_pos
    self.row_idx = row_idx

  def check_collision(self, item):
    
    if item.pos == self.pos:
      if type(item) == Coin:
        self.coins += 1
      elif type(item) == Shell:
        self.health -= 20
        self.health = max(0, self.health)
      elif type(item) == Heart:
        self.health = 100
      elif type(item) == Bomb:
        self.health = 0

    if self.health <= 0:
      self.char = emoji.emojize(':collision:')

  def decrement_health(self):
    self.health -= 1
    
    # Check for coins
    if self.coins >= 5:
      self.health = 100
      self.coins = 0

  def print_status(self):
    print(f"Kart status | health: {self.health} | coins: {self.coins}")

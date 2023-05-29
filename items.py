import emoji 

class Coin:
  def __init__(self, start_pos):
    self.char = emoji.emojize(':money_bag:')
    self.pos = start_pos

class Shell:
  def __init__(self, start_pos):
    self.char = emoji.emojize(':turtle:')
    self.pos = start_pos

class Heart:
  def __init__(self, start_pos):
    self.char = emoji.emojize(':blue_heart:')
    self.pos = start_pos

class Bomb:
  def __init__(self, start_pos):
    self.char = emoji.emojize(':bomb:')
    self.pos = start_pos

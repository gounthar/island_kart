from items import Coin, Shell, Heart, Bomb
from map_row import MapRow
import random
from map import Map
import time

class RaceSim:
  def __init__(self, map_height, map_width):
    self.num_steps = 0
    self.dir_step_change = 10 # number of steps between a direction change
    self.step_dir = 'straight'
    self.map = Map(map_height, map_width)

  def generate_course_step(self):
    # Choose direction
    if self.num_steps % self.dir_step_change == 0:
      self.step_dir = random.choice(['left', 'right', 'straight'])

    new_course_pos = self.map.rows[0].course_pos
    new_row = MapRow(self.map.width, new_course_pos)
    if self.step_dir == 'left':
      new_row.increment_course_pos(-2)
    elif self.step_dir == 'right':
      new_row.increment_course_pos(2)
    
    new_row.make_course_poles()
    self.map.wipe_kart()
    self.map.cycle_rows()
    self.map.rows[0] = new_row

    # Create coin
    coin_thresh = 0.2
    if random.uniform(0,1) < coin_thresh:
      self.make_item("coin")

    # Create shell
    shell_thresh = 0.4
    if random.uniform(0,1) < shell_thresh:
      self.make_item("shell")

    # Create heart
    heart_thresh = 0.02
    if random.uniform(0,1) < heart_thresh:
      self.make_item("heart")

    # Create bomb
    bomb_thresh = 0.2
    if random.uniform(0,1) < bomb_thresh:
      self.make_item("bomb")
  
  def make_item(self, item):
    
    # Choose from even positions
    start_pos = self.map.rows[0].course_pos + random.choice(range(0, self.map.rows[0].course_width-1, 2)) + 2
    
    # Don't allow duplicate positions
    if any(existing_item.pos == start_pos for existing_item in self.map.rows[0].items):
      return
    
    if item == "coin":
      new_item = Coin(start_pos)
    elif item == "shell":
      new_item = Shell(start_pos)
    elif item == "heart":
      new_item = Heart(start_pos)
    elif item == "bomb":
      new_item = Bomb(start_pos)
    
    self.map.rows[0].add_item(new_item)

  def check_collision(self):
    # Check last row
    kart_row = self.map.rows[self.map.kart.row_idx]
    if len(kart_row.items) > 0:
      for item in kart_row.items:
        self.map.kart.check_collision(item)

  def display_course(self):
    self.map.wipe_kart()
    self.map.make_kart()
    self.map.display()

  def step(self, key_press):
    self.generate_course_step()
    self.map.move_kart(key_press)
    self.map.make_kart()
    
    self.map.kart.decrement_health()
    self.num_steps += 1

  def detect_end(self):
    if self.map.kart.health <= 0:
      print("GAME OVER")
      print(f"Score: {self.num_steps - 1}")
      print(f"Press ESC to exit")
      return True
    return False    

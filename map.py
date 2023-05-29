from map_row import MapRow
import math
from kart import Kart
from pynput.keyboard import Key

class Map:
  def __init__(self, map_height, map_width):
    self.height = map_height
    self.width = map_width

    self.rows = [MapRow(self.width) for i in range(self.height)]

    # Kart starts in last row
    start_pos = self.rows[-1].course_pos + math.floor(self.rows[-1].course_width / 2) + 2
    if start_pos % 2 != 0:
      start_pos = max(0, start_pos - 1)
    self.kart = Kart(start_pos, self.height-1)

  def move_kart(self, key_press):

    new_row_idx = self.kart.row_idx
    new_kart_pos = self.kart.pos

    # Check input
    if key_press == Key.right:
      new_kart_pos += 2
    elif key_press == Key.left:
      new_kart_pos -= 2
    elif key_press == Key.up:
      new_row_idx -= 1
    elif key_press == Key.down:
      new_row_idx += 1

    # Clamp to course width
    self.kart.row_idx = max(0, min(self.height-1, new_row_idx))
    row = self.rows[self.kart.row_idx]
    left_bound = row.course_pos + 2
    right_bound = row.course_pos + row.course_width
    if new_kart_pos % 2 != 0:
      new_kart_pos -= 1
    self.kart.pos = max(left_bound, min(right_bound, new_kart_pos))
    

  def display(self):
    for row_idx,row in enumerate(self.rows):
      # Clear row
      row.make_course_poles()
      
      # Insert items
      for item in row.items:
        if row_idx == self.kart.row_idx:
          if type(item) is not Kart and item.pos == self.kart.pos:
            continue
        n_items_left = row.n_items_left(item.pos)
        row.data = row.data[:item.pos - n_items_left] + item.char + row.data[item.pos + 2 - n_items_left:]
      
      # Display row
      print(row.data)
  
  def cycle_rows(self):
    self.rows.pop()
    self.rows.insert(0, MapRow(self.width))

  def make_kart(self):
    self.rows[self.kart.row_idx].add_item(self.kart)

  def wipe_kart(self):
    # Wipe item
    for i in range(len(self.rows[self.kart.row_idx].items)):
      if type(self.rows[self.kart.row_idx].items[i]) == Kart:
        self.rows[self.kart.row_idx].items.pop(i)
        break

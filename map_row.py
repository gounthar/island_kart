import math
from kart import Kart

class MapRow:
  def __init__(self, map_width, course_pos=None, course_width=20):
    self.width = map_width
    self.course_width = course_width
    self.default_course_pos = math.floor((self.width - self.course_width - 2) / 2)
    if course_pos is None:
      self.course_pos = self.default_course_pos
    else:
      self.course_pos = course_pos
    
    self.char_map_bound = '#'
    self.char_course_bound = '|'

    self.data = self.make_blank_row_data()

    self.items = []

  def make_blank_row_data(self):
    new_data = self.char_map_bound + ' ' * self.width + self.char_map_bound
    return new_data
  
  def add_item(self, item):
    # Add item and keep items sorted left-to-right by position
    self.items.append(item)
    self.items.sort(key=lambda x: x.pos)
  
  def make_course_poles(self):
    
    left_spaces = " " * self.course_pos
    right_spaces = " " * (self.width - self.course_pos - self.course_width - 2)
    course_poles = self.char_course_bound + " " * self.course_width + self.char_course_bound

    self.data = self.char_map_bound + left_spaces + course_poles + right_spaces + self.char_map_bound
  
  def n_items_left(self, pos):
    n_items_left = 0
    for item in self.items:
      if item.pos < pos:
        n_items_left += 1
    return n_items_left

  def update_course_pos(self, new_course_pos, new_course_width):
    if 0 <= new_course_pos and new_course_pos <= (self.width - new_course_width - 2):
      self.course_width = new_course_width
      self.course_pos = new_course_pos

  def increment_course_pos(self, inc):
    self.update_course_pos(self.course_pos + inc, self.course_width)

  def valid_pos(self, pos):
    if 0 <= pos and pos <= (self.width - 2):
      return True
    return False




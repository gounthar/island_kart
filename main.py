import time
import threading
from pynput import keyboard
from pynput.keyboard import Key
from race_sim import RaceSim
import math
import random

key_press = None # global variable for user input
def run_game():
  map_height = 20
  map_width = 50
  sim = RaceSim(map_height, map_width)
  sleep_sec = 0.3
  global key_press

  # While not at end of course
  while not sim.detect_end():
    # Return to exit game
    if key_press == Key.esc:
      return

    # Step world
    num_left = math.floor((map_width - 3) / 2)
    num_right = map_width - num_left - 3
    print('\n' + '=' * num_left + f' {sim.num_steps:03d} ' + '='*num_right)
    sim.step(key_press)

    # React
    sim.check_collision()

    # Display
    sim.display_course()
    sim.map.kart.print_status()

    # Prepare for next iteration
    if key_press is not None:
      key_press = None
    time.sleep(sleep_sec)
  
  # print('\n' + '=' * num_left + f' {sim.num_steps:03d} ' + '='*num_right)
  # sim.display_course()
  # sim.map.kart.print_status()
  return

def on_key_press(key):
    global key_press
    key_press = key
    if key == Key.esc:  
      exit()   

def main():
  thread2 = threading.Thread(target=run_game, args=())
  thread2.start()

  with keyboard.Listener(on_press=on_key_press) as listener:
      listener.join()

if __name__ == '__main__':
  random.seed(1)
  main()
from sense_hat import SenseHat
from datetime import datetime, timedelta
from time import sleep

sense = SenseHat()

datetime_original = datetime(year=2021, month=1, day=1,hour=0,minute=0,second=0)
seconds_to_add = 10
seconds_to_subtract = -10

b = [0,0,0]
r = [255,0, 0]
o = [255,165,0]
s = [255,204,153]
y = [255,255,0]
w = [255,255,255]

explosion1 = [
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, y, y, b, b, b,
b, b, y, w, w, y, b, b,
b, b, y, w, w, y, b, b,
b, b, b, y, y, b, b, b,
b, b, b, b, b, b, b, b,
b, b, b, b, b, b, b, b,
]

explosion2 = [
b, b, b, b, b, b, b, b,
b, b, o, s, s, o, b, b,
b, o, s, y, y, s, o, b,
b, s, y, w, w, y, s, b,
b, s, y, w, w, y, s, b,
b, o, s, y, y, s, o, b,
b, b, o, s, s, o, b, b,
b, b, b, b, b, b, b, b,
]

explosion3 = [
b, b, b, r, r, b, b, b,
b, r, o, s, s, o, r, b,
b, o, s, y, y, s, o, b,
r, s, y, w, w, y, s, r,
r, s, y, w, w, y, s, r,
b, o, s, y, y, s, o, b,
b, r, o, s, s, o, r, b,
b, b, b, r, r, b, b, b,
]

print("""Set your time:
  1)press 'up' to add 10s
  2)press 'down' to deduct 10s
  3)press 'right' to see the current time of the timer
  4)press 'middle' to start the timer
""")

while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        datetime_original += timedelta(seconds = seconds_to_add)
      elif event.direction == "down" and datetime_original.minute >= 0 and datetime_original.second > 0:
        datetime_original += timedelta(seconds = seconds_to_subtract)
      elif event.direction == "right":
        current_timer = datetime_original.strftime("%M:%S")
        sense.show_message(current_timer, scroll_speed = 0.05, text_colour=[0,255,255])
      elif event.direction == "middle":
        while not datetime_original.second == 0:
          current_timer = datetime_original.strftime("%S")
          sense.show_message(current_timer, scroll_speed = 0.045, text_colour=[0,255,255])
          datetime_original += timedelta(seconds = -1)
        sense.set_pixels(explosion1)
        sleep(0.3)
        sense.set_pixels(explosion2)
        sleep(0.3)
        sense.set_pixels(explosion3)
        sleep(2)
        sense.clear()

#TODO synchronize the counter with a real clock and let the display show it accordingly

#TODO add sound when it explodes

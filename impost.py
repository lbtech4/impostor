import pyautogui as pg, os, time
def chat():
    pg.click(x=979, y=466)
    time.sleep(1)
    pg.hotkey('alt', 'h')

def sendMes(mes):
    pg.typewrite(mes)
    pg.press("enter")

def allow():
  t = pg.locateOnScreen("pw.png")
  if (t is not None):
    commandr = "not allowed"
    return commandr
  elif (t is None):
    commandr = "in meeting"
    return commandr 

def connect(url):
  os.system(f"start {url}")
  time.sleep(2)
  pg.press("tab", presses=2, interval=1)

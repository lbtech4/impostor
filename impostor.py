import pyautogui, os, time
#logan/lbtech4

def allow():
  t = pyautogui.locateOnScreen("pw.png")
  if (t is not None):
    commandr = "not allowed"
    return commandr
  elif (t is None):
    commandr = "in meeting"
    return commandr 
  
  
 #can use while (allow() == "not allowed"): to wait
def connect(url):
  os.system(f"start {url}")
  pyautogui.moveTo(pyautogui.locateOnScreen("join.png")); time.sleep(1); pyautogui.click()
  
def openChat():
  pyautogui.click(pyautogui.locateOnScreen("chat.png")
                  
def sendMessage(mes):
 pyautogui.typewrite(mes)
 pyautogui.press("enter")

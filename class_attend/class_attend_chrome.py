import time, argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

parser = argparse.ArgumentParser(description = 'Get the day order.')
parser.add_argument('-d', '--dayorder', type = int, nargs = '?', default = False,
                    help = 'The day order for which to run the script.')
args = parser.parse_args()

if args.dayorder is not False:

  if args.dayorder >= 1 and args.dayorder <= 6:
    day_order = args.dayorder - 1
  
  else:
    parser.error("day order can only be from 1 to 6")

else:
  day_order = int(input("What Day order is it "))  - 1

# Email to join the meet from.
email_value = <email>

# Password for the account.
pwd_value = <password>

meet = r'https://meet.google.com/'

# Data is a list of dictionaries. Each dictionary's key is current hour which 
# return a Gmeet code and a nested list with end time. Empty slots are False.

data = [

  { 9: ["fdr65oczjr", [10, 40]],
    10: ["fdr65oczjr", [10, 40]],
    11: ["gzr5zxcgwq", [11,59]],
    12: ["MEET code goes here", [False, 59]],
    13: ["gnj6ch45ga", [13,59]],
    14: ["dqajocgb2s", [15, 30]]
  },
  {
    9: ["ftu4im256o", [10, 40]],
    10: ["ftu4im256o", [10, 40]],
    11: ["fdr65oczjr", [11,59]],
    12:["MEET code goes here", [False, 59]],
    13: ["gzr5zxcgwq", [13,59]],
    14: ["fp4bbewafy", [15, 30]]
  },
  {
    9: ["amnpq3yssi", [10, 40]],
    10: ["amnpq3yssi", [10, 40]],
    11:["hheruvzyor", [11, 59]],
    12:["MEET code goes here", [False, 59]],
    13: ["eoeben7fr6", [13,59]]
  },
  {
    9: ["eoeben7fr6", [10, 40]],
    10: ["eoeben7fr6", [10, 40]],
    11: ["amnpq3yssi", [11,59]],
    12: ["MEET code goes here", [False, 59]],
    13: ["fdr65oczjr", [13,59]],
    14: ["amnpq3yssi", [15, 30]]
  },
  {
    9: ["ev4gplxqal", [10, 40]],
    10: ["ev4gplxqal", [10, 40]],
    11: ["eoeben7fr6", [11,59]],
    12:["MEET code goes here", [False, 59]],
    13:["MEET code goes here", [False, 59]],
    14: ["gxmbn2tybn", [15, 30]]
  },
  {
    9: ["gnj6ch45ga", [10, 40]],
    10: ["gnj6ch45ga", [10, 40]],
    11: ["ev4gplxqal", [11,59]],
    12:["MEET code goes here", [False, 59]],
    13: ["amnpq3yssi", [13,59]],
    14: ["gzr5zxcgwq", [15, 30]]
  }
]

# The options.add_argument is the defualt user profile that 
# could be found in a path similar to:
# Linux distros: /home/<username>/.config/google-chrome/Default
# Windows: need to add
options = Options()
options.add_argument(<user profile>)

# Try adjusting this so when chrome window open you see the sign-in button.
options.add_argument("window-size=1200,900")

while_flag = True
while(while_flag):
  try:
    # Get current and date time.
    time_now = datetime.now()

    # Format time into H:M format.
    cur_time = time_now.strftime("%H:%M")

    # Assigning seperate variables for hrs and minutes.
    cur_hr = int(time_now.strftime("%H"))
    cur_min = int(time_now.strftime("%M"))

    # Assigning ending hour and ending minute variables for cleaner understandable code.
    end_hour = data[day_order][cur_hr][1][0]
    end_min = data[day_order][cur_hr][1][1]

    if not end_hour:
      print(f"Waiting for next Lecture coming up in {(end_min - cur_min)} minutes")
      time.sleep(60)
      continue

    elif (cur_hr <= end_hour):
      if(cur_min < end_min ):
        print('entered')
        print(data[day_order][cur_hr][0])

        # Get chromedriver from https://chromedriver.chromium.org/
        # and add it as a PATH variable or specify the path in the
        # next line in the executable_path argument. 
        driver = webdriver.Chrome(executable_path = "./chromedriver", desired_capabilities = DesiredCapabilities.CHROME,
                                  chrome_options = options)
        driver.implicitly_wait(5)
        driver.get(meet)


        time.sleep(4)
        # Element for sign-in button.
        sign_in = driver.find_element_by_css_selector("span.cta-wrapper:nth-child(1) > a:nth-child(1)")
        sign_in.click()

        time.sleep(4)
        # Element to find email field.
        email = driver.find_element_by_css_selector('#identifierId')
        email.send_keys(email_value)

        # To click next on the email page.
        email_nxt = driver.find_element_by_css_selector('.VfPpkd-RLmnJb')
        email_nxt.click()

        # Element to find password field.
        time.sleep(8)
        pwd =  driver.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)') 
        pwd.send_keys(pwd_value)

        # To click next on the email page.
        pwd_next = driver.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)')
        pwd_next.click()
        time.sleep(4)

        # Join or start a meeting button.
        join_start = driver.find_element_by_class_name("cmvVG")
        join_start.click()
        time.sleep(2)

        # Here the Gmeet code is passed to the code field on the Gmeet page.
        code_field = driver.find_element_by_css_selector(".poFWNe")
        code_field.send_keys(data[day_order][cur_hr][0])
        
        # Continue button after entering the code.
        cont = driver.find_element_by_css_selector(".Y5sE8d > span:nth-child(3) > span:nth-child(1)")
        cont.click()

        time.sleep(5)
        # Disabling the video stream if on otherwise if off will turn it on.
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("e").perform()

        # Disabling the mic stream if on otherwise if off will turn it on.
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("d").perform()

        # To join the meeting.
        time.sleep(4)
        join = driver.find_element_by_css_selector(".NPEfkd")
        join.click()

        while(True):
          time.sleep(5)
          time_now = datetime.now()
          cur_time = time_now.strftime("%H:%M")
          cur_hr = int(time_now.strftime("%H"))
          cur_min = int(time_now.strftime("%M"))
          if (cur_hr == end_hour):
            if(cur_min >= end_min):
              # Close the browser.
              driver.close()
              break
      else:
          print(f'Waiting for Next Lecture in {59 - cur_min} minutes')
          time.sleep(60)
          continue
  except KeyError:
    if cur_hr>=16:
      exit()
  except IndexError:
    print("Please Input Correct Day Order Press ctrl+c to exit")

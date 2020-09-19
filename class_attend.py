from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime 

#email to join the meet from
email_value = r'ak9169@srmist.edu.in'

#password for the account
pwd_value = r''

meet = r'https://apps.google.com/intl/en-GB/meet/'

#put your data here in format {"class code": ["meet code without dash"],[start hour, start min],[end hour, end min]}
data = {"A": ["sgozwrhztb",[12,40],[12,50]], "C": ["nicgtjnzmk",[6,56],[6,58]], "D": ["eoeben7fr6",[11,2],[12,0]]}

profile = webdriver.FirefoxProfile('/home/aakash/.mozilla/firefox/hyabzzaw.default')
profile = FirefoxProfile()
profile.set_preference('devtools.jsonview.enabled', False)
profile.set_preference('dom.webdriver.enabled', False)
profile.set_preference('useAutomationExtension', False)
profile.set_preference('media.navigator.permission.disabled', True)
profile.update_preferences()


for slot in data:
  
  while_flag = True
  while(while_flag):

    cur_time = datetime.now()
    cur_hr = cur_time.timetuple()[3]
    cur_min = cur_time.timetuple()[4]
    if ((cur_hr >= data[slot][1][0] and cur_min >= data[slot][1][1]) and (cur_hr <= data[slot][2][0] and cur_min <= data[slot][2][1])):
      
      driver = webdriver.Firefox(desired_capabilities=DesiredCapabilities.FIREFOX, firefox_profile=profile)
      driver.get(meet)


      #time.sleep(4)
      #Element for sign-in button.
      sign_in = driver.find_element_by_css_selector("span.cta-wrapper:nth-child(1) > a:nth-child(1)")
      sign_in.click()

      time.sleep(4)
      #Element to find email field
      email = driver.find_element_by_css_selector('#identifierId')
      email.send_keys(email_value)

      #To click next on the email page 
      email_nxt = driver.find_element_by_css_selector('.VfPpkd-RLmnJb')
      email_nxt.click()

      #Element to find passwrod field
      time.sleep(4)
      pwd =  driver.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)') 
      pwd.send_keys(pwd_value)

      #To click next on the email page
      pwd_next = driver.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)')
      pwd_next.click()
      time.sleep(4)

      #Join or start a meeting button
      join_start = driver.find_element_by_class_name("cmvVG")
      join_start.click()
      time.sleep(2)

      #Meet code entering field
      code_field = driver.find_element_by_css_selector(".poFWNe")
      code_field.send_keys(data[slot][0])

      #Continue button after entering the code.
      cont = driver.find_element_by_css_selector(".Y5sE8d > span:nth-child(3) > span:nth-child(1)")
      cont.click()

      time.sleep(5)
      #disabling the video stream if on otherwise if off will turn it on
      webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("e").perform()

      #disabling the mic stream if on otherwise if off will turn it on
      webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("d").perform()

      time.sleep(4)
      #To join the meeting
      join = driver.find_element_by_css_selector(".NPEfkd")
      join.click()

      while_flag_1 = True
      while(while_flag_1):
        time.sleep(5)
        cur_time = datetime.now()
        cur_hr = cur_time.timetuple()[3]
        cur_min = cur_time.timetuple()[4]
        if (data[slot][2][0] == cur_hr and data[slot][2][1] == cur_min):
          #close the whole window
          driver.close()
          while_flag = False

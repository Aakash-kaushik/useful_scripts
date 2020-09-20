# Guide for setting up the script(class_attend.py)

**The Script only works on Firefox as of now**

## Getting Gecko Drivers
- Download [Gecko Drivers](https://github.com/mozilla/geckodriver/releases) and add them as a PATH variable
- [How to Add Path varaible for windows](https://www.youtube.com/watch?v=ADh_OFBfdEE)
- I'm trusting linux users

## Setting Firefox profile

- linux distros: /home/<username>/.mozilla/firefox/<Random_Letters>.default
- windows: C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\<Random_Letters>.default

once you find your firefox profile dir,  copy and replace <profile-path> on Line 81
>profile = webdriver.FirefoxProfile(r'<profile-path>')

## You're all set, run the script in your shell
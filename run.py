from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Starting Browser... ")

browser = webdriver.Firefox()
# For Chrome: browser = webdriver.Chrome()
# For Safari: browser = webdriver.Safari()
# For Firefox: browser = webdriver.Firefox()

print("en: Loggining... ")
browser.get("https://roblox.com/login")
username = browser.find_element(By.ID, "login-username")
password = browser.find_element(By.ID, "login-password")

username.send_keys("cnaotic_individual") # Type Roblox Account Nickname here
password.send_keys("ragemode343") # Type Roblox Account Password here

voiti = browser.find_element(By.ID, "login-button")
voiti.click()
time.sleep(10)

x = 7
y = 8
x += 3

while x >= y:
 f = open("id.txt", "r+")
 prosm = int(f.read())
 print("Following... ")
 browser.get(f"https://roblox.com/users/{prosm}")
 tritochki = browser.find_element(By.ID, "popover-link")
 tritochki.click()
 time.sleep(2)
 podpis = browser.find_element(By.ID, "profile-follow-user")
 podpis.click()
 time.sleep(2)
 af = str(prosm - 1)
 f.truncate(0)
 f.seek(0)
 f.write(af)
 print("FOLLOWED! JUMPING TO ID: " + af )
 f.close()
 time.sleep(3)

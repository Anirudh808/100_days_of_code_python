from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 10)
got_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/a[1]')))
got_button.click()

language = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]')))
language.click()

cookie = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bigCookie"]')))

play_time_start = datetime.now().timestamp()
print(play_time_start)
play_duration = 60
is_game_on = True

while is_game_on:
    cookie = driver.find_element(By.ID, 'bigCookie')
    cookie.click()
    if datetime.now().timestamp() >= play_time_start + play_duration:
        is_game_on = False




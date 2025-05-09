from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.top')))

first_name = driver.find_element(By.CSS_SELECTOR, 'input.top')
first_name.send_keys("Anirudh")

last_name = driver.find_element(By.CSS_SELECTOR, 'input.middle')
last_name.send_keys("Mounasamy")

email = driver.find_element(By.CSS_SELECTOR, 'input.bottom')
email.send_keys("anirudhmounasamy@gmail.com")

submit = driver.find_element(By.TAG_NAME, "button")
submit.send_keys(Keys.ENTER)

# driver.quit()

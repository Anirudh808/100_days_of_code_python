from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.amazon.in/Xiaomi-Redmi-Flexible-Silicone-Emodil/dp/B0BRWJ1V1F/ref=sr_1_6?crid=2WHGTG3FK5MFU&dib=eyJ2IjoiMSJ9.86-W2CF3B24Wk0BI8CX7FfkWbW5fNCdx1VW8EV-58ubdvcRdwSzC6HXnynYP2Gvf_8kugSFFf8VFFfJ7OnIhLQxY8D3idDmeKxCMR_tvyKpFX83_o-iANwdgnu7JxR5AX1vmjjpBpT8gCAOrSUyIxxY-ZHmidW-HJA9L0kF2xrNf1w1vVKYPg1WT3ykHhklhNXUWiHvC-yv_d8pTocE1VZksJxwyJZDCllSEJJGt6fo.pTjRVs5n-zVcpSiyLfIOTsnMgLFEgPVkoRCJG4uKTDQ&dib_tag=se&keywords=poco%2Bx5pro%2Bback%2Bcover&qid=1746766185&sprefix=poco%2Bx5pro%2Bb%2Caps%2C322&sr=8-6&xpid=OtA50ejuzgZul&th=1"
new_url = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(new_url)

# skip_captcha = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/div/div[2]/a')
# skip_captcha.click()

wait = WebDriverWait(driver, 10)
upcoming_events = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'event-widget')))

upcoming_events_list = upcoming_events.find_elements(By.CSS_SELECTOR, "li")

upcoming_events_dict = {}

for index, event in enumerate(upcoming_events_list):
    date = event.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime").split("T")[0]
    event_name = event.find_element(By.CSS_SELECTOR, "a").text
    # print(f"{date}: {event_name}")
    upcoming_events_dict[index] = {date: event_name}

print(upcoming_events_dict)

driver.quit()

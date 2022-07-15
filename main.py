from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = r"C:\Users\ugott\Desktop\Learning Mats\100 Days of Code\Day-48-Selenium-Game Bot\Selenium Drivers for Chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
start_time = time.time()
old_time = time.time()
game_on = True

upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
upgrade_dict = {}


def cookie_check():
    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))
    for count, item in enumerate(upgrades):
        try:
            add = int(item.text.split("- ")[1].replace(',',
                                                       ''))  # Split the string to the number. Then remove the comma. The convert to int
        except:
            continue

        upgrade_dict[count] = add

    for val in range(len(upgrade_dict.values())):
        if money > upgrade_dict[val]:
            pass
        else:
            select_upgrade = driver.find_elements(By.CSS_SELECTOR, "#store b")[val - 1]
            select_upgrade.click()
            return


while game_on:
    cookie.click()

    if time.time() - old_time >= 5:
        cookie_check()
        old_time = time.time()


    elif time.time() - start_time >= 300:
        game_on = False

cps = driver.find_element(By.ID, "cps").text
print(cps)

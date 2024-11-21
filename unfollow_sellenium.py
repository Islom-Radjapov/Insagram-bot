from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Log in to Instagram
driver.get("https://www.instagram.com/")
time.sleep(3)

# Input your credentials
username = "afarmleniya_shar_wedding"
password = "sora1234"

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys(username)
password_input.send_keys(password)
username_input.submit()
time.sleep(5)

# Navigate to profile
driver.get(f"https://www.instagram.com/{username}/")
time.sleep(3)

# Open the "Following" list
try:
    following_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/following/')]"))
    )
    following_button.click()
    time.sleep(5)
except Exception as e:
    print(f"Failed to open 'Following' list: {e}")
    driver.quit()
    exit()

for _ in range(1000):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Following']]"))
        )
        button.click()
        time.sleep(5)
        print("Clicked the 'Following' button successfully.")
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Locate and click the "Unfollow" button using its class attributes
        button = driver.find_element(By.XPATH, "//button[contains(@class, '_a9--') and contains(@class, '_ap36') and contains(@class, '_a9-_')]")
        button.click()
        time.sleep(5)
        print("Clicked the 'unfollow' button successfully.")
    except Exception as e:
        print(f"Error: {e}")

    try:
        driver.execute_script("window.scrollTo(612, 581)")
        print("Scroling")
    except Exception as e:
        print("Error scroling  ", e)
    time.sleep(5)


print("Finished unfollowing.")
driver.quit()

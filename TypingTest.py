from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
os.environ["PATH"] += os.pathsep + r'../Downloads/chromedriver_win32/'


try:
    driver = webdriver.Chrome()
    driver.get("https://10fastfingers.com/typing-test/english")

    # Wait for the page to fully load
    time.sleep(6)

    # Find the text input element on the page
    text_input = driver.find_element("id", "inputfield")

    # Find all the words to type
    words = driver.find_elements("xpath", "//span[@wordnr]")

    # Type each word into the input field
    for word in words:
        text_to_type = word.text
        for character in text_to_type:
            text_input.send_keys(character)
            time.sleep(0)
        text_input.send_keys(" ")
        time.sleep(0)

    # Submit the form to complete the typing test
    text_input.send_keys(Keys.RETURN)

except Exception as e:
    print("An error occurred:", e)

    # finally:
    #     Close the web browser
    # driver.quit()
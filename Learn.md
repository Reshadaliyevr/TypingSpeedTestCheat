# 10FastFingers Typing Speed Test Automation - Learn

Welcome to the learning guide for the 10FastFingers Typing Speed Test Automation project! This guide will teach you about the functionality of the script and how it works.

## Project Overview

The 10FastFingers Typing Speed Test Automation script allows you to automate the typing speed test on the 10FastFingers website. The script uses Selenium WebDriver to control a web browser and automatically types the words from the test using simulated keyboard input.

## Project Components

The project consists of the following main components:

1. `automate_typing_speed_test.py`: This Python script is responsible for automating the typing speed test. It uses the Selenium WebDriver to interact with the 10FastFingers website and simulate typing.

2. `chromedriver`: The chromedriver executable is required to automate the Google Chrome browser. The script uses the chromedriver to control the browser and perform automated actions.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Selenium library (`pip install selenium`)
- Google Chrome browser

## How the Script Works

The script follows these steps to automate the typing speed test:

1. Launches the Google Chrome browser using the chromedriver executable.

2. Navigates to the 10FastFingers typing test page.

3. Waits for 6 seconds to allow you to accept or deny cookies on the website.

4. Locates the text input element on the page.

5. Finds all the words to type for the test.

6. Simulates typing each word into the input field character by character.

7. Adds a space after typing each word to separate them.

8. Submits the form to complete the typing speed test.

## Running the Script

To run the script and automate the typing speed test, follow these steps:

1. Ensure that you have the necessary prerequisites installed on your system.

2. Download the `automate_typing_speed_test.py` script and the chromedriver executable.

3. Open the script in a text editor and update the `os.environ["PATH"] += os.pathsep + r'path/to/chromedriver'` line with the correct path to the chromedriver executable on your system.

4. Save the changes to the script.

5. Open a terminal or command prompt and navigate to the directory where the script is located.

6. Run the script using the following command:

``` python TypingTest.py ```


7. Sit back and relax as the script automatically completes the typing speed test on 10FastFingers.

## Customization

You can customize the behavior of the script by modifying the following variables in the `automate_typing_speed_test.py` script:

- `NUM_ROUNDS`: The number of test rounds to perform.
- `ROUND_DELAY`: The delay (in seconds) between each test round.
- `SHOW_BROWSER`: Set to `True` if you want to see the browser window while the script runs. Set to `False` for headless execution.

Feel free to explore and modify the script to suit your needs.

## Disclaimer

This script is intended for educational and personal use only. Use it responsibly and in accordance with the terms and conditions of the 10FastFingers website. The author is not responsible for any misuse or violation of the website's policies.

---

Congratulations! You have successfully learned how to use and understand the 10FastFingers Typing Speed Test Automation script. Enjoy automating your typing speed tests!

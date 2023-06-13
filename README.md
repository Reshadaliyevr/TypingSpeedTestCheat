# 10FastFingers Typing Speed Test Automation

This Python script automates the typing speed test on the website [10FastFingers](https://10fastfingers.com/typing-test/english). It allows you to quickly complete the typing test by automatically typing the words from the test using simulated keyboard input.

## Features

- Automates the typing speed test on 10FastFingers.
- Uses Selenium WebDriver to control the web browser.
- Supports Google Chrome browser using the chromedriver executable.
- Automatically types the words from the test using simulated keyboard input.

## Requirements

- Python 3.x
- Selenium library (`pip install selenium`)

## Usage

1. Make sure you have Python and the Selenium library installed.
2. Download the chromedriver executable and ensure it is added to your system's PATH variable.
3. Clone or download the script from this repository.
4. Open the script in a text editor and update the chromedriver path in the line `os.environ["PATH"] += os.pathsep + r'../Downloads/chromedriver_win32/'` to the appropriate path on your system.
5. Save the script and close the text editor.
6. Open a terminal or command prompt and navigate to the directory where the script is located.
7. Run the script using the following command:
``` python automate_typing_speed_test.py ```
8. Sit back and relax as the script automatically completes the typing speed test on 10FastFingers.

## Disclaimer

This script is intended for educational and personal use only. Use it responsibly and in accordance with the terms and conditions of the 10FastFingers website. The author is not responsible for any misuse or violation of the website's policies.

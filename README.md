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
7. Customize the `time.sleep(6)` value to set the desired waiting time when the website is initially loaded. Adjusting this value allows you to extend or reduce the pause duration before the typing speed test begins. By providing an adequate waiting time, you can ensure sufficient time to handle any cookie consent prompts or website loading delays, ensuring smooth automation of the typing speed test.
8. You can modify the values on lines 26 and 28 to adjust the typing speed during the test. By increasing or decreasing the `time.sleep()` values, you can control the delay between each character typed, resulting in a slower or faster input pace. Experimenting with these values allows you to fine-tune the typing speed simulation according to your preference or specific testing requirements.
9. Run the script using the following command:
``` python TypingTest.py ```
8. Sit back and relax as the script automatically completes the typing speed test on 10FastFingers.

## Disclaimer

This script is intended for educational and personal use only. Use it responsibly and in accordance with the terms and conditions of the 10FastFingers website. The author is not responsible for any misuse or violation of the website's policies.

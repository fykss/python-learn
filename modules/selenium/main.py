# Documnetation: https://selenium.dev/documentation/en/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    browser = webdriver.Chrome(
        '/Users/vladyslavlietun/Documents/Projects/Python/Introduction/modules/selenium/chromedriver')
    browser.get('https://selenium.dev')
    downloads = browser.find_element_by_link_text('Downloads')
    downloads.click()
    search_bar = browser.find_element_by_name('search')
    search_bar.send_keys('Downloads')
    search_bar.send_keys(Keys.ENTER)


if __name__ == '__main__':
    main()

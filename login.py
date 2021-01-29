import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as cond

def shutdown(driver):
    print('Shutting down.')
    driver.quit()
    sys.exit(0)

def setup():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('w3c', False)
        driver = webdriver.Chrome('/usr/bin/chromedriver',options=chrome_options)
        driver.get("https://chesstempo.com")
        driver.set_window_size(1440, 900)
    except:
        shutdown(driver)
        
def main():
    try:

        try:
            login_tap=driver.find_element_by_id('ct-login-show-button')
        except NoSuchElementException:
            print('cannot find login element')
        print('found the login button!')
        login_tap.click()
        #WebDriverWait(driver,10).until(cond.visibility_of(login_tap))

        try:
            username_field = driver.find_element_by_id('ct-login-username-field')
        except NoSuchElementException:
            print('cannot find the username field.')
        username_field.send_keys('unclevinny')
        password_field = driver.find_element_by_id('ct-login-password-field')
        password_field.send_keys('houmesx')
        login_button = driver.find_element_by_id('ct-login-button')
        login_button.click()

        # now we should be able to find the user profile page
        try:
            profile = driver.find_element_by_css_selector('[aria-label=unclevinny user menu]')
            print('found the profile element!')
        except NoSuchElementException:
            print('No luck finding the profile element.')
            shutdown(driver)   

if __name__ == '__main__': main()

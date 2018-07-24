from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def setDriver():
    CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # chrome path
    #CHROME_PATH = r"C:\Users\Tarc\AppData\Local\Google\Chrome\Application\chrome.exe"
    CHROMEDRIVER_PATH = r"C:\chromedriver_win32\chromedriver.exe" # driver path
    #ADBLOCK_PATH = r"C:\Users\Hard-\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\cfhdojbkjhnklbpkdaibdccddilifddb"
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
    #chrome_options.add_argument('--disable-popup-blocking')
    #chrome_options.add_argument('load-extention='+ADBLOCK_PATH)
    #chrome_options.add_extension('Adblock-Plus_v3.1.crx')
    chrome_options.binary_location = CHROME_PATH        
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    browser.get("https://freemidi.org/genre-pop")
    items = browser.find_elements_by_class_name("genre-link-text")

    count = 0
    for item in items:
        print(count)
        print(item.find_element_by_xpath(".//*").text)
        browser.find_element_by_class_name("artist-song-cell").click()
        browser.find_element_by_id("downloadmidi").click()
        time.sleep(3)
        browser.back()
        browser.back()
        count+=1
    browser.quit()

setDriver()
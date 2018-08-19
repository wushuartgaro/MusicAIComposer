from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import winsound


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


def setDriver():
    CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # chrome path
    #CHROME_PATH = r"C:\Users\Tarc\AppData\Local\Google\Chrome\Application\chrome.exe"
    CHROMEDRIVER_PATH = r"C:\chromedriver_win32\chromedriver.exe" # driver path
    #ADBLOCK_PATH = r"C:\Users\Hard-\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\cfhdojbkjhnklbpkdaibdccddilifddb"
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('load-extention='+ADBLOCK_PATH)
    chrome_options.binary_location = CHROME_PATH        
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    
    browser.get("https://freemidi.org/topmidi")
    items = browser.find_elements_by_class_name("genre-link-text")
    count = 1
    count2 = 1
    songs_count = 1
    visitedLists = []
    songs = browser.find_elements_by_class_name("top-mid-title")
    visitedSongs = []
    for song in songs:
        visitedSongs.append(song.get_attribute('innerHTML'))
        count+=1
        if count > 50:
            break
            
    for available_song in visitedSongs:
        musics = browser.find_elements_by_class_name("top-mid-title")
        for music in musics:
            if music.get_attribute('innerHTML') == available_song:
                music.click()
                browser.find_element_by_id("downloadmidi").click()
                print(count2, " song(s)")
                time.sleep(3)
                count2+=1
                browser.back()
                break

    browser.quit()

    """
    songs = browser.find_elements_by_class_name("artist-song-cell")
    visitedSongs = []
    for song in songs:
        visitedSongs.append(song.get_attribute('innerHTML'))
            
    for available_song in visitedSongs:
        musics = browser.find_elements_by_class_name("artist-song-cell")
        for music in musics:
            if music.get_attribute('innerHTML') == available_song:
                music.click()
                browser.find_element_by_id("downloadmidi").click()
                print(count2, " song(s)")
                time.sleep(3)
                count2+=1
                browser.back()
                break

    for i in range(0, len(items)):
        visitedLists.append(items[i].get_attribute('innerHTML'))

    for available_click in visitedLists:
        elements = browser.find_elements_by_class_name("genre-link-text")
        for element in elements:
            songs_count = 1
            if element.get_attribute('innerHTML') == available_click:
                name = element.get_attribute('innerHTML')
                print("==============================================")
                print(count," artist(s)")
                print("==============================================")
                element.click()
                print("clicked")
                songs = browser.find_elements_by_class_name("artist-song-cell")
                if len(songs) > 9:
                    print("This artist: " + str(count) + " name: "+ name)
                for song in songs:
                    visitedSongs.append(song.get_attribute('innerHTML'))
                
                for available_song in visitedSongs:
                    musics = browser.find_elements_by_class_name("artist-song-cell")
                    for music in musics:
                        if music.get_attribute('innerHTML') == available_song:
                            music.click()
                            browser.find_element_by_id("downloadmidi").click()
                            print(count2, " song(s)")
                            time.sleep(3)
                            count2+=1
                            browser.back()
                            break
                count+=1
                browser.back()
                
                break
    
    browser.quit()
    """
    #winsound.Beep(frequency, duration)

setDriver()
import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller

def main():
    chromedriver_autoinstaller.install()
    
    chrome_options = Options()
    chrome_options.add_argument("--detach")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options = chrome_options)
    
    URL = input("Enter the post URL:")

    driver.get(URL)

    wait = WebDriverWait(driver, 2)

    comments = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#-post-rtjson-content p")))
    
    f = codecs.open("reddit_comments.txt", "a", "utf-8")
    try:
        for element in comments:
            comment = element.get_attribute("innerText") 
                
            f.write(comment + "\n\r")
            
    except:
        f.write("" + "\n\r")
    f.close()
    driver.quit()
if __name__ == "__main__":
    main()















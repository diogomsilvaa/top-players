import pandas as pd 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DataCollection:

    def __init__(self):
        #self.df = pd.DataFrame()
        #self.df.columns = ["Name", "Club", "League", "League Goals", "League Assists", "UCL Goals", "UCL Assists", "UEL Goals", "UEL Assists", "UcL Goals", "UcL Assists", "Continental Goals", "Continental Assists", "WorldCup Goals", "WorldCup Assists", "Confederations Goals", "Confederations Assists", "ClubWorldCup Goals", "ClubWorldCup Assists", "SuperCups Goals", "SuperCups Assists", "Qualifications Goals", "Qualification Assists", "NationalCups Goals", "NationalCups Assists"]
        pass


    def init_browser(self):
        opts = Options()
        opts.headless = True;
        self.browser = webdriver.Firefox(options=opts)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def close_browser(self):
        self.browser.close()
    
    
        
class TransferMarkt(DataCollection):

    def __init__(self):
        super().__init__()
        self.playersNames = []
        self.playersLinks = []

    def accept_cookies(self):
        frame = self.browser.find_element(By.ID, "sp_message_iframe_575843")
        self.browser.switch_to.frame(frame)
        button = self.browser.find_element(By.CLASS_NAME, "sp_choice_type_11")
        button.click()
        self.browser.switch_to.default_content()


    def getTop250(self):
        url = "https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
        self.browser.get(url)
        time.sleep(2)
        self.accept_cookies()
        nrLoops = 10
        for _ in range(nrLoops):
            container =  self.browser.find_element(By.ID, "yw1")
            table = container.find_element(By.TAG_NAME,"tbody")
            names_links = table.find_elements(By.TAG_NAME, "a")
            for nl in range(1, len(names_links), 4):
                self.playersNames.append(names_links[nl].text)
                self.playersLinks.append(names_links[nl].get_attribute("href"))
            
            arrow = container.find_element(By.CLASS_NAME, "tm-pagination__list-item--icon-next-page")
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            arrow.click()
            time.sleep(1)

    def getPlayerInfo():
        pass

    def printPlayersInfo(self):
        for i in range(250):
            print(str(i) + ":")
            print("Name: " + self.playersNames[i])
            print("Link: " + self.playersLinks[i])


            

    
import shutil
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException



# creating a new folder location for today
downloadPath = "D:\\Fred_Data\\"
new_folder = os.path.join(downloadPath, datetime.now().strftime("%Y_%m_%d"))

try:
    os.mkdir(new_folder)
except:
    shutil.rmtree(new_folder)
    os.mkdir(new_folder)


# configuring downloadPath
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": new_folder,
           "download.directory_upgrade": True,
           "download.prompt_for_download": False
         }

# driver settings
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)


def download_fed_csv(econ_data_code):

    '''
    Takes a econ time series code from the st. louis fed website
    and downloads the csv to the download location
    :return: csv file location
    '''

    fred_url = "https://fred.stlouisfed.org/series/"
    driver.get(fred_url+econ_data_code)
    time.sleep(2)

    try:
        driver.find_element(By.XPATH,"//*[@id='download-button']" ).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='download-data-csv']").click()

    except NoSuchElementException:
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='download-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='download-data-csv']").click()

    time.sleep(5)


# looping through list
data_codes = ["CPIAUCSL", "GDP"]

for code in data_codes:
    download_fed_csv(code)


driver.close()





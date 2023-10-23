import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from google.oauth2.service_account import Credentials
import gspread

option = Options()
driver = webdriver.Chrome(options=option)

driver.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('Auth.json', scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("Data").sheet1

for i in range(0, 99999):
    try:
        Department_name = driver.find_element(By.XPATH, "/html/body/c-wiz/div/main/c-wiz/div[3]/c-wiz/c-wiz[" + str(i) + "]/c-wiz/div/article/h4").text
        Post_Time = driver.find_element(By.XPATH, "/html/body/c-wiz/div/main/c-wiz/div[3]/c-wiz/c-wiz[" + str(i) + "]/c-wiz/div/article/div[3]/time").text
        print(Department_name)
        print(Post_Time)
        sheet.update_acell('A' + str(i + 1), Department_name)
        sheet.update_acell('B' + str(i + 1), Post_Time)
    except NoSuchElementException:
        pass

# Close the webdriver when you're done
driver.quit()

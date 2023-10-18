import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from oauth2client.service_account import ServiceAccountCredentials

import gspread

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

driver.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
# time.sleep(20)

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Auth.json', scope)
file=gspread.authorize(credentials=ServiceAccountCredentials)
sheet=file.open("Data")
sheet=sheet.sheet1


for i in range(0,99999):
    try:
        Department_name = driver.find_element(By.XPATH, "/html/body/c-wiz/div/main/c-wiz/div[3]/c-wiz/c-wiz[" + str(i) + "]/c-wiz/div/article/h4").text
        # Description=driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div/4/div[2]/div/div/div[2]/div/div["+str(i)+"]/div/div/div[2]/div/p").text
        # Country=driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div["+str(i)+"]/div/div/div[2]/ul/li[2]/a").text
        Post_Time=driver.find_element(By.XPATH,"/html/body/c-wiz/div/main/c-wiz/div[3]/c-wiz/c-wiz[" + str(i) + "]/c-wiz/div/article/div[3]/time").text
        # Image=driver.find_element(By.XPATH,"/html/body/div[8]/div/div/div[4]/div[2]/div/div/div[2]/div/div["+str(i)+"]/div/div/div[1]/div/div/img")
        # Image_url = Image.get_attribute("src")
        print(Department_name)
        # print(Description)
        # print(Country)
        print(Post_Time)
        # print("Image URL:", Image_url)
        sheet.update_acell('A'+str(i+1),Department_name)
        sheet.update_acell('B'+str(i+1),Post_Time)
    except NoSuchElementException:
        pass

# Close the webdriver when you're done
driver.quit()
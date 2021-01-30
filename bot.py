from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

def LogIn(driver, username, pasword) :
    driver.find_element_by_id("user").send_keys(username)
    driver.find_element_by_id("parola").send_keys(pasword)
    driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    sleep(3)

driverFirefox = webdriver.Firefox(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_geckodriver-v0.29.0-win64.zip\geckodriver.exe")
driverFirefox.get("https://www.pbinfo.ro/")
LogIn(driverFirefox, "500_IQ", "exemplu1")

pyautogui.moveTo(70, 700);
pyautogui.doubleClick()
sleep(1)

for i in range(545, 3800):


    UrlSolOF = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id=" + str(i)
    driverFirefox.get(UrlSolOF)
    sleep(3)

    if not "problema invalid" in driverFirefox.page_source:
        SolvedProblem = driverFirefox.find_element_by_xpath("//*[@id=\"zona-mijloc\"]/div/div[10]/div[2]/pre")
        SolvedProblem.click()
        SolvedProblem.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        SolvedProblem.send_keys(Keys.CONTROL, 'c')
        sleep(1)

        pyautogui.moveTo(1300, 300);

        pyautogui.rightClick()
        pyautogui.hotkey('w', 't')

        pyautogui.typewrite(str(i))

        pyautogui.press('enter')
        sleep(2)

        pyautogui.press('down')
        pyautogui.press('up')

        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 's')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)

    else :
        pyautogui.moveTo(1300, 300);

        pyautogui.rightClick()
        pyautogui.hotkey('w', 't')

        pyautogui.typewrite(str(i))

        pyautogui.press('enter')
        sleep(2)

        pyautogui.press('down')
        pyautogui.press('up')

        pyautogui.press('enter')
        sleep(0.5)
        pyautogui.typewrite("Sorry, we do not have this problem yet! We ll try to fix this as soon as we can! Thanks")
        sleep(0.5)
        pyautogui.hotkey('ctrl', 's')
        sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        sleep(0.5)


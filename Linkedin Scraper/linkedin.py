from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# setup webdriver
def setupWebDriver(url):
    chromeDriverPath = Service("/Users/manwell/Development/chromedriver")
    driver = webdriver.Chrome(service=chromeDriverPath)
    driver.get(url)
    return driver

def automatedBotConnectCall(candidateAccountLink):

    candidateNameLink = driver.find_element(By.LINK_TEXT,)
    #detect the connect button
    connectButton = driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[2]/button[1]")
    connectButton.click()


def login(username,loginPassword):
    email = driver.find_element(By.ID, "session_key")
    email.send_keys(username)

    password = driver.find_element(By.ID, "session_password")
    password.send_keys(loginPassword)

    password.send_keys(Keys.ENTER)

#checks if the account found is private
def privateAccount(personAttribute):
    if personAttribute is None:
        return True
    else:
        return False
def storeInfo(driver):
    counter = 1
    peopleNames = []
    accounts = {}

    #automatic action
    driver.implicitly_wait(5)
    searchBar = driver.find_element(By.CLASS_NAME,"search-global-typeahead__input")
    searchBar.send_keys("Software Engineer")
    searchBar.send_keys(Keys.ENTER)

    # ADD A DELAY HERE TO LET THE PAGE LOAD
    driver.implicitly_wait(20)
    peopleButton = driver.find_element(By.XPATH,"html/body/div[4]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button")
    peopleButton.click()
    peopleUserNames = driver.find_elements(By.CLASS_NAME,"reusable-search__result-container")
    for n in peopleUserNames:
        accounts[n]={
            "Full Name": driver.find_element(By.XPATH,f'//*[@id="main"]/div/div/div[1]/ul/li[{counter}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text,
            "Job Title": driver.find_element(By.XPATH,f'//*[@id="main"]/div/div/div[1]/ul/li[{counter}]/div/div/div[2]/div[1]/div[2]/div/div[1]').text,
            "Location": driver.find_element(By.XPATH,f'//*[@id="main"]/div/div/div[1]/ul/li[{counter}]/div/div/div[2]/div[1]/div[2]/div/div[2]').text,
            # "LinkedIn URL":driver.find_element(By.LINK_TEXT,driver.find_element(By.XPATH,f'//*[@id="main"]/div/div/div[1]/ul/li[{counter}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text)
        }
        counter+=1
        #//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a
        #//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[2]/div/div[1]
        #//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[2]/div/div[2]
        #//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[2]/p
        #//*[@id="main"]/div/div/div[1]/ul/li[1]/div/div/div[2]/div[2]
        #//*[@id="main"]/div/div/div[1]/ul/li[2]/div/div/div[2]/div[2]
    return accounts
    #
    #
    # #filling the dictionary with accounts gathered from webpage
    # for n in range(len(peopleNames)):
    #     if not privateAccount(driver.find_element(By.NAME,peopleId)):
    #         accounts[n]={
    #             "Full Name" : driver.find_element(By.NAME,"className.name"),
    #             "Email" : driver.find_element(By.CLASS_NAME,"socialmediaPlatformEmailClassName"),
    #             "Job Title" : driver.find_element(By.ID,"socialMediaPlatformJobTitleID"),
    #             "Platform Account": peopleNames[n].getName()
    #             }
    #     else:
    #         automatedBotConnectCall(driver.find_element(By.LINK_TEXT,"platformLinkTest"))
    #
    #
    # return accounts,peopleNames
#input("please enter your email")
username = ""
#input("please enter your password")
password =  ""


driver = setupWebDriver(f"https://www.linkedin.com/")
login(username,password)
gatheredAccounts = storeInfo(driver)

print(gatheredAccounts)

#automatic action
print(driver.current_url)

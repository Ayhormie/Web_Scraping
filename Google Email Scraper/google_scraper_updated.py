from bs4 import BeautifulSoup
import requests
import re
import pandas as pd








def scrapeGoogleGeneral(url_to_scrape):
    """
    Params: 
     # url_to_srape: URL of google results page
       to be scraped for emails

    Returns:
     # list of dictionaries containing database row data
    """
    pageText = str(pullTextFromPage(url_to_scrape))
    email_without_space=r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
    email_with_space=r"[a-zA-Z0-9\.\-+_]+@\s[a-z0-9\.\-+_]+\.[a-z]+"
    
    set_of_emails = set(re.findall(email_without_space, str(pageText)) + re.findall(email_with_space, str(pageText)))

    if(set_of_emails):
        new_email_set = removeSpaces(set_of_emails)
        dict_list =  createDictList(url_to_scrape, new_email_set)
        return dict_list
    else:
        return None


def pullTextFromPage(url_to_scrape):
    """
    Params:
     # url_to_srape: URL of google results page to be scraped for emails

    Returns:
     # <class 'bs4.element.ResultSet'> containing all divs from provided webpage
    """
    req = requests.get(url_to_scrape, 'lxml')
    soup = BeautifulSoup(req.text, 'lxml')
    obj = soup.find_all("div", string=True)
    return obj

def removeSpaces(set_of_emails):
    """
    Params:
     # set_of_emails: set() containing strings (emails) pulled from webpage

    Returns:
     # new_email_sate: set() containing strings (emails) pulled from webpage,
       without the spaces
    """
    new_email_set = set()
    for item in set_of_emails:
        new_email_set.add(item.replace(' ', ''))
    return new_email_set

def createDictList(url, email_set):
    """
    Params:
     # url: url of scraped page
     # email_set: set of emails with spaces removed

    Returns:
     # row_data_list: list of dictionaries containing (column name: row data) pairs
    """
    row_data_list = []
    for email in email_set:
        row = {'url':url + " - " + email, 'email': email, 'date':str(pd.to_datetime("today").date())}
        row_data_list.append(row)
    # return row_data_list
    return email_set






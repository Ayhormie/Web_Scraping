from bs4 import BeautifulSoup
import requests
import re


def scrape_google_resumes(google_url):
    """
    Params:
     # google_url: url to a google query results page

    Returns:
     # row_data_list: list of dictionaries containing row data
    """
    row_data_list = []

    for link in get_github_resume_links(google_url):
        try:
            row_data_list.append(parse_git_resume(link))
        except:
            pass

    return row_data_list

def get_github_resume_links(google_url):
    """
    Params: 
     # google_url: url to a google results page containing
       links to github resumes

    Returns:
     # cleaned_links: a list containing links to
       webpages with github resumes
    """
    pulled_links = []
    cleaned_links = []
    start = '/url?q='
    end = '&'
    
    for link in scrape_hrefs(google_url):
        if(link.has_attr('href') and "/url?q=" in link['href']):
            pulled_links.append(link['href'])

    for link in pulled_links:
        if('google' not in link):
            try:
                cleaned_links.append(link[link.index(start)+len(start):link.index(end)])
            except:
                pass

    return cleaned_links


def scrape_hrefs(query_to_scrape):
    """
    Params:
     # google_url: url to a google results page containing
       links to github resumes 

    Returns:
     # <class 'bs4.element.ResultSet'> containing all HTML anchor tags 
       with https://gist.github.com/ in the tag's href attribute
    """
    
    query_page = requests.get(query_to_scrape)
    soup = BeautifulSoup(query_page.text, 'html.parser')
    scraped_hrefs = soup.find_all('a', href=re.compile("https://gist.github.com/"))
    return scraped_hrefs


def parse_git_resume(resume_link):
    """
    Params:
     # resume_link: link to gist.github webpage containing a resume

    Returns:
     # list with one dictionary containing row data
    """
    page = requests.get(resume_link)
    
    stripped_strings = list(get_strings_from_html(page.content))
    if(stripped_strings == None):
        return None
    resume_info = get_top_of_resume(stripped_strings)

    skillset = get_skills(stripped_strings)
    row_info = {'url': resume_link,  'resume': resume_info,'skills': skillset}
    return row_info


def get_strings_from_html(html):
    """
    Params:
     # html: html of a github resume page
    
    Returns:
     # article_list: list of strings containing 
       data from 'article' elements in an HTML page
    """
    soup = BeautifulSoup(html, "html.parser")

    try:
        article = soup.find('article')
        for data in article(['style', 'script']):
            data.decompose()
    except:
        return []

    article_list = article.stripped_strings
    return article_list

def get_top_of_resume(stripped_strings):
    """
    Params:
     # stripped_strings: a list of lines of text (strings) pulled from a github resume

    Returns:
     # top_of_resume: first 5 strings within that list
    """
    top_of_resume = stripped_strings[0:5]
    return top_of_resume

def get_skills(top_five_resume_lines):
    """
    Params:
     # resume_lines: list of strings (lines of text) pulled from a github resume
    
    Returns:
     # skillset: set of skill words (strings) contained within resume_lines
    """
    list_of_skills = [#languages
                  'sql', 'c', 'c++', 'azure',  'javascript',  'python', 'java', 'c#', 'html', 'css', 'react',
                  'bootstrap', 'ios', 'flask', 'node.js',
                  #skills
                  'web developer', 'web development', 'mobile', 'backend', 'back-end', 'frontend', 'front-end', 
                  'fullstack', 'full-stack', 'data science', 'data scientist', 'machine learning', 'ai', 
                  #tools
                  'aws', 'excel', 'git', 'version control', 'android studio', 
                   ]
    skillset = set()

    for skill in list_of_skills:    
        for line in top_five_resume_lines:
            if skill in line.lower():
                skillset.add(skill.lower())

    return skillset



















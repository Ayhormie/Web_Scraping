from github_scraper_updated import scrape_google_resumes



def main():
    """
    To use, simply query google for github resumes and paste the link to the results page below.
    
    It's recommended that the google query contains 'site:https://gist.github.com/' and '@_____.com'
    For example:
        site:https://gist.github.com/ software developer microsoft @gmail.com
    
    """
    google_result_url = "paste URL here (within quotes)"
    results = scrape_google_resumes(google_result_url)
    print(results)






if __name__ == '__main__':
    main()
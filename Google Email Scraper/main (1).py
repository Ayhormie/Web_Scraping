from google_scraper_updated import scrapeGoogleGeneral

#Query: software developer melbourne site:linkedin.com '@gmail.com'
test_url1 = "https://www.google.com/search?q=software+developer+melbourne+site%3Alinkedin.com+%40gmail.com&biw=1920&bih=933&sxsrf=ALiCzsYup8lBv_5xAj9XGfaZaVWtfdq2ow%3A1659336128066&ei=wHXnYp_UA_OsqtsPh_uxoAs&ved=0ahUKEwiftOfjhKX5AhVzlmoFHYd9DLQQ4dUDCA8&uact=5&oq=software+developer+melbourne+site%3Alinkedin.com+%40gmail.com&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAUoECEYYAFDWBliWF2CjG2gBcAB4AIABb4gB2AGSAQMwLjKYAQCgAQHAAQE&sclient=gws-wiz-serp"

#Query: data scientist harvard site:linkedin.com '@gmail.com'
test_url2 = "https://www.google.com/search?q=data+scientist+harvard+site%3Alinkedin.com+%27%40gmail.com%27&sxsrf=ALiCzsb03f1NY1qbHWFyaTSrLFIcoJiaGA%3A1658968709246&ei=hdrhYunBDu25qtsP5cSr6As&ved=0ahUKEwipmO6ErJr5AhXtnGoFHWXiCr0Q4dUDCA4&uact=5&oq=data+scientist+harvard+site%3Alinkedin.com+%27%40gmail.com%27&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6CggAEEcQsAMQyQM6BwgAELADEENKBQg8EgEzSgQIQRgASgQIRhgAUN0KWI5eYK53aANwAXgAgAG9AogB_RySAQgwLjI0LjAuMZgBAKABAqABAcgBCsABAQ&sclient=gws-wiz"

#Query: "careers@*.com" 
test_url3 = "https://www.google.com/search?q=careers%40&biw=1536&bih=877&sxsrf=ALiCzsZUmxZ77SdN2EFJ3oAjOz07WLfSHQ%3A1658973229090&ei=LezhYu30BIaaptQPoaGYmAw&ved=0ahUKEwitv4vwvJr5AhUGjYkEHaEQBsM4ZBDh1QMIDg&uact=5&oq=careers%40&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoFCC4QkQI6EQguEIAEELEDEIMBEMcBENEDOgUILhCABDoLCAAQgAQQsQMQgwE6BwguENQCEEM6BQgAEJECOgQIABBDOgsILhCABBDHARDRAzoECC4QQzoOCC4QgAQQxwEQ0QMQ1AI6BwguELEDEEM6CAgAEIAEELEDOg4ILhCxAxCDARDHARDRAzoICAAQsQMQkQI6CwguEIAEELEDEIMBOhAIABCABBCHAhCxAxCDARAUOgsIABCxAxCDARCRAjoOCAAQgAQQsQMQgwEQyQM6BQgAEJIDOgQIABAeSgUIPBIBNEoECEEYAEoECEYYAFCLlQFYkc8BYNrTAWgEcAF4AIABrAGIAbwJkgEDMC45mAEAoAEByAEIwAEB&sclient=gws-wiz"

#Query: github jason "@gmail." com
test_url4 = "https://www.google.com/search?q=github+jason+%22@gmail.%22+com&sa=X&ved=2ahUKEwiPzsv405r5AhXylWoFHR0XAxYQ5t4CegQICBAB&biw=1920&bih=933&dpr=1"

#Query: "careers@" site:indeed.com software
test_url5 = "https://www.google.com/search?q=%22careers%40%22+site%3Aindeed.com+software&sxsrf=ALiCzsa-BQLVSipWJI943Jrh_fLUhJz1Qw%3A1658986016207&ei=IB7iYp2XDOmXwbkPy9GziA4&ved=0ahUKEwidp7vB7Jr5AhXpSzABHcvoDOEQ4dUDCA4&uact=5&oq=%22careers%40%22+site%3Aindeed.com+software&gs_lcp=Cgdnd3Mtd2l6EANKBQg8EgExSgQIQRgBSgQIRhgAUHBYxA1gyQ5oAXAAeACAAa0BiAH-CJIBAzAuOJgBAKABAcABAQ&sclient=gws-wiz"

#Query: "careers@" site:glassdoor.com
test_url6 = "https://www.google.com/search?q=%22careers%40%22+site%3Aglassdoor.com&sxsrf=ALiCzsbIMcTAyI_I5sg17b9Txgu4C4G4Uw%3A1658990209212&ei=gS7iYsjNDLSKwbkPp8OCgAc&ved=0ahUKEwiIkuyQ_Jr5AhU0RTABHaehAHAQ4dUDCA4&uact=5&oq=%22careers%40%22+site%3Aglassdoor.com&gs_lcp=Cgdnd3Mtd2l6EANKBQg8EgEySgQIQRgBSgQIRhgAUPAbWLApYKUraAJwAHgAgAFxiAGeCZIBBDEwLjOYAQCgAQHAAQE&sclient=gws-wiz"

#Query: site: instagram.com software developer @gmail.com
test_url7 = "https://www.google.com/search?q=site%3Ainstagram.com+software+developer+%40gmail.com&sxsrf=ALiCzsYSyvc1bl04H-8s1sOJpFXthuOIWg%3A1659309301576&source=hp&ei=9QznYu-cHeXUkPIPgPqD8Ao&iflsig=AJiK0e8AAAAAYucbBX0SSAEKBKpt3f-1BstDhIxVUva3&ved=0ahUKEwiv6_LroKT5AhVlKkQIHQD9AK4Q4dUDCAo&uact=5&oq=site%3Ainstagram.com+software+developer+%40gmail.com&gs_lcp=Cgdnd3Mtd2l6EAM6BAgjECc6EQguEIAEELEDEIMBEMcBENEDOgsILhCABBDHARDRAzoRCC4QgAQQsQMQxwEQ0QMQ1AI6CAgAELEDEIMBOgsIABCABBCxAxCDAToICC4QgAQQsQM6CAguELEDEIMBOgQIABBDOg0ILhDHARDRAxDUAhBDOg4ILhCABBCxAxDHARDRAzoQCC4QsQMQgwEQxwEQ0QMQQzoHCAAQsQMQQzoOCC4QgAQQxwEQrwEQ1AI6BwguENQCEEM6CgguEMcBENEDEEM6CAgAEIAEELEDOgsILhCABBDHARCvAToICAAQgAQQyQM6BQgAEJIDOgsILhCSAxDHARCvAVAAWK5JYOFKaABwAHgAgAG7AYgBhSuSAQQ3LjQxmAEAoAEB&sclient=gws-wiz"







def main():
    # insert link to google search below
    url = "url here"
    print(scrapeGoogleGeneral(test_url7))
    
    







if __name__ == "__main__":
    main()
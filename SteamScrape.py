from bs4 import BeautifulSoup
import requests

'''
returns data in dictionary
from key = title
vale = (image, discount, discounted price)
'''
class SteamScrape:

    def nl_stripper():
        pass

    def get_data():
        data = {}
        url = "https://store.steampowered.com/search/?specials=1"
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.content, 'html.parser')
        search_resultsRows = soup.find('div', {"id": "search_resultsRows"})
        href = search_resultsRows.find_all(href = True)
        for item in href:
            title = ((item.find('span', {"class": "title"})).contents)[0]
            image = ((item.find('div', {"class": "col search_capsule"})).img)['src']
            discount = ((item.find('div', {"class": "col search_discount responsive_secondrow"})).text).strip()
            discounted_price_div = (item.find('div', {"class": "col search_price discounted responsive_secondrow"}))
            if discounted_price_div is not None:
                discounted_price = str((discounted_price_div.contents[len(discounted_price_div)-1]).strip())
            else:
                discounted_price = "N/A"
            data[title] = (image, discount, discounted_price)
        return data

if __name__ == "__main__":
    print(SteamScrape.get_data())

from bs4 import BeautifulSoup
import requests


def get_data():

    data = {}
    url = "https://store.steampowered.com/search/?specials=1"
    # pulls the html from the website to parsed by bs4
    html_doc = requests.get(url)

    # scrapes the url for all steam sales
    soup = BeautifulSoup(html_doc.content, 'html.parser') 
    search_results_rows = soup.find('div', {"id": "search_resultsRows"})
    href = search_resultsRows.find_all(href = True)

    # searches the href tag and finds the title, image, and discounts on all items in the sale
    for item in href:
        title = ((item.find('span', {"class": "title"})).contents)[0]
        image = ((item.find('div', {"class": "col search_capsule"})).img)['src']
        discount = ((item.find('div', {"class": "col search_discount responsive_secondrow"})).text).strip()
        discounted_price_div = (item.find('div', {"class": "col search_price discounted responsive_secondrow"}))
    
        # some items in the discount list arent actually discounted this removes all non discounted items
        if discounted_price_div is not None:
            discounted_price = str((discounted_price_div.contents[len(discounted_price_div)-1]).strip())
        else:
            discounted_price = "N/A"

        # sorts items into dictionary with tile as the key and tuple value
        data[title] = (image, discount, discounted_price)
    return data


if __name__ == "__main__":
    print(get_data())

import requests
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    total_quotes = len(quotes)
    # print(total_quotes)
    authors = []
    tags_list = []
    quotes_with_is = 0

    for quote in quotes:

        text = quote.find('span', class_='text').get_text()

    # print(text)

        author = quote.find('small', class_='author').get_text()
        # print(author)
        authors.append(author)

        tags = quote.find('div', class_='tags').find_all('a', class_='tag')
        for tag in tags:
            tags_list.append(tag.get_text())
        # print(tag.get_text())

        if "is" in text.lower():
            quotes_with_is += 1

    unique_authors = len(set(authors))

    # author with most quotes

    tag_counts = (len(tags_list))

    print("=== QUOTE ANALYSIS RESULTS ===")
    print(f"Total number of quotes: {total_quotes}")
    print(f"Number of unique authors: {unique_authors}")
    print(f"Quotes containing 'is': {quotes_with_is}")
    print(tags_list)

else:
    print(
        f"Failed to retrieve the webpage. Status code: {response.status_code}")

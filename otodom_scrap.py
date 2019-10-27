import bs4 as bs
from urllib.request import Request, urlopen

# url = 'https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?page='

# lista z linkami do podstron, z których każda zawiera 24 mieszkania
page_links = []

# lista z linkami do poszczególnych mieszkań
flat_links = []

def get_links_list(url):

    req = Request(url, headers={'User-Agent': 'Mozilla/6.0'})
    otodom_html = urlopen(req).read()

    otodom_soup = bs.BeautifulSoup(otodom_html, 'lxml')

    flat_adverts = otodom_soup.findAll('div', {'class': "offer-item-details"})

    for flat_advert in flat_adverts:
        # link do szczegółów
        flat_link = flat_advert.find('a').attrs['href']
        flat_links.append(flat_link)
    # print('List of links to individual flats saved')

def get_page_list(url):
    for page in range(20,25,1):
        page_links.append(url + str(page))
    print('List of links to pages saved')
    print(page_links)

# zacznij kolejny scrap od 25

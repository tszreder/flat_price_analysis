import bs4 as bs
from urllib.request import Request, urlopen
from flat_class import Flat

features = []
flat_rows = []

# urls =['http://otodom.pl/oferta/38-m2-metro-brodno-po-kapitalnym-remoncie-ID42WoV.html#c89760baae',
#        'http://otodom.pl/oferta/38-m2-metro-brodno-po-kapitalnym-remoncie-ID42WoV.html#c89760baae']


def ScrapDetails(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/6.0'})
    flat_html = urlopen(req, timeout=50).read()

    flat_soup = bs.BeautifulSoup(flat_html, 'lxml')

    seller = flat_soup.find('div', {'class' : 'css-7hnk9y'}).text
    title = flat_soup.find('h1', {'class': 'css-18igut2'}).text
    location = flat_soup.find('a', {'class' : 'css-1dliymu'}).text.split(';}')[2]
    price = flat_soup.find('div', {'class' : 'css-1vr19r7'}).text.split(' zł')[0].replace(' ', '')
    price_per_sq = flat_soup.find('div', {'class' : 'css-18q4l99'}).text.replace(' ', '').split('zł')[0]

    details = flat_soup.find('div', {'class' : 'css-1ci0qpi'}).findAll('li')

    area, rooms, market, building_type, floor, total_floors, material, year_built, ownership_type = \
        [None, None, None, None, None, None, None, None, None]

    for detail in details:
        if detail.text.find('Powierzchnia') != -1:
            area = detail.find('strong').text.split(' ')[0]
        elif detail.text.find('Liczba pokoi') != -1:
            rooms = detail.find('strong').text
        elif detail.text.find('Rynek') != -1:
            market = detail.find('strong').text
        elif detail.text.find('Rodzaj zabudowy') != -1:
            building_type = detail.find('strong').text
        elif detail.text.find('Piętro') != -1:
            floor = detail.find('strong').text
        elif detail.text.find('Liczba pięter') != -1:
            total_floors = detail.find('strong').text
        elif detail.text.find('Materiał budynku:') != -1:
            material = detail.find('strong').text
        elif detail.text.find('Rok budowy:') != -1:
            year_built = detail.find('strong').text
        elif detail.text.find('Forma własności:') != -1:
            ownership_type = detail.find('strong').text
        else:
            pass

    flat_row = Flat(seller, title=title, location=location, price= price, price_per_sq= price_per_sq,
                    area=area, rooms= rooms, market= market, building_type=building_type, floor=floor,
                    total_floors=total_floors, material=material, year_built=year_built,
                    ownership_type=ownership_type)

    flat_rows.append(vars(flat_row).values())

    # return flat_row

# for url in urls:
#     ScrapDetails(url)

# print(flat_rows)
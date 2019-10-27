from otodom_scrap import get_links_list, flat_links, page_links, get_page_list
from scrap_one_flat import ScrapDetails, flat_rows
from csv_writer import write_to_csv

page_counter = 0

url = 'https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?nrAdsPerPage=72&page='

# scraping a list of links to pages with adverts
get_page_list(url)

# scraping a list of links from the first page of adverts
for link in page_links:
    page_counter += 1
    get_links_list(link)
    print(str(page_counter) + ' page scraped')

# entering into each link and scraping the necessary details from the advert and saving as objects of class Flat
for link in flat_links:
    ScrapDetails(link)

# print(flat_rows)

# saving all flats to csv file
write_to_csv(flat_rows)
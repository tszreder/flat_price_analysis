import csv

# from scrap_one_flat import  flat_rows

def write_to_csv(csvData):

    titles = ['seller', 'title', 'location', 'price', 'price_per_sq',
                     'area',
                     'rooms',
                     'market',
                     'building_type',
                     'floor',
                     'total_floors',
                     'material',
                     'year_built',
                     'ownership_type']

    # csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
    # csvData = [vars(flat_row).values()]
    # csvData = flat_rows
    with open('flats.csv', 'a', encoding='utf8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows([titles])
        writer.writerows(csvData)
    csvFile.close()
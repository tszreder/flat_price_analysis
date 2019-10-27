import pandas as pd
import numpy as np

def load_clean_data(csv):

    df = pd.read_csv(csv)

    data = df.drop(columns=['title', 'material'])


    # usunięcie nawiasów powstałych przy scrapingu
    for column in data.columns:
        data[column] = data[column].str.replace("\(\'", '')
        data[column] = data[column].str.replace("\'\,\)", '')
        data[column] = data[column].replace("Brak danych", np.nan)

    # zamiana nietypowych wartości w kolumnie floors na wartości liczbowe
    data['floor'] = data['floor'].str.replace("parter", '0')
    data['floor'] = data['floor'].str.replace("> 10", '10')
    data['floor'] = data['floor'].str.replace('więcej niż 10', '10')

    # print(data['floor'].value_counts())
    # print(data['total_floors'].value_counts())


    numeric_columns = ['price', 'price_per_sq', 'area', 'rooms', 'floor', 'total_floors', 'year_built']

    # zamiana przecinków na kropki w kolumnach numerycznych i konwersja typu na float
    for column in numeric_columns:
        data[column] = data[column].str.replace(",", '.')
        data[column] = pd.to_numeric(data[column], errors='coerce')
        data[column] = data[column].astype(float)

    #rozdzielenie lokalizacji i zatrzymanie tylko nazwy dzielnicy
    data['location'] = data['location'].str.split(',', expand= True)[1]

    # print(data.isna().sum())



    # print(data['rooms'].value_counts())

    data = data.drop(columns=['building_type', 'year_built', 'ownership_type'])

    data = data.dropna(axis='index')


    # OneHotEncode the remaining object variables
    model_data = pd.get_dummies(data, prefix=['seller', 'loc', 'market'],
                          columns=['seller', 'location', 'market'])

    # Create a separate dataset without result and a separate with just the target variable
    target = model_data['price_per_sq']
    model_data = model_data.drop(columns='price_per_sq')

    # Change the target variable from discrete to categorical
    price_bins = [0, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 100000]
    labels = ['<7000','7001-8000','8001-9000','9001-10000',
              '10001-11000','11001-12000','12001-13000','13001-14000', '14001-15000', '>15000']
    # price_bins = [5000, 7000,9000, 11000,  13000,  15000, 100000]
    # labels = ['5001-7000','7001-9000','9001-11000',
    #           '11001-13000','13001-15000', '>15000']

    target_binned = pd.cut(target, bins=price_bins, labels=labels)

    # Standardize all the variables
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()

    model_data = pd.DataFrame(scaler.fit_transform(model_data))
    return model_data, target_binned, target, data


# load_clean_data('flats.csv')

# data = load_clean_data('flats.csv')[0]
# target_bin = load_clean_data('flats.csv')[1]
# target = load_clean_data('flats.csv')[2]
# print(data.dtypes)
# print(target.dtypes)

# print(data)
# print(data.isna().sum())
# print(target_bin.isna().sum())
# print(target.isna().sum())
#
# print(target.value_counts().sort_index())







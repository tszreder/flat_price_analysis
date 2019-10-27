
def brak_danych_if_none(val):
    if val is None:
        return 'Brak danych'
    else:
        return val


class Flat:

    def __init__(self, seller, title, location, price,
                 price_per_sq,
                 area,
                 rooms,
                 market,
                 building_type,
                 floor,
                 total_floors,
                 material,
                 year_built,
                 ownership_type):

            self.seller = brak_danych_if_none(seller)
            self.title= brak_danych_if_none(title)
            self.location = brak_danych_if_none(location)
            self.price = brak_danych_if_none(price)
            self.price_per_sq = brak_danych_if_none(price_per_sq)
            self.area = brak_danych_if_none(area)
            self.rooms = brak_danych_if_none(rooms)
            self.market = brak_danych_if_none(market)
            self.building_type = brak_danych_if_none(building_type)
            self.floor = brak_danych_if_none(floor)
            self.total_floors = brak_danych_if_none(total_floors)
            self.material = brak_danych_if_none(material)
            self.year_built = brak_danych_if_none(year_built)
            self.ownership_type = brak_danych_if_none(ownership_type)



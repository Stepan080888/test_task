class SearchModel:
    def __init__(self, car, region, city):
        self.car = car
        self.region = region
        self.city = city

    def __repr__(self):
        return "%s " % (self.car)

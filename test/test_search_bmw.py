import pytest
from fixture.app import Application
from model.searchmodel import SearchModel

test_value = [SearchModel(car='BMW', region='Киевская область', city='Киев')]

@pytest.mark.parametrize('test_object', test_value, ids=[repr(i) for i in test_value])
def test_search_by_city(app, test_object):
    app.search.fill_in_car(test_object.car)
    app.search.fill_in_city_and_press_search(region=test_object.region, city=test_object.city)
    app.search.configure_search(money='$', sort_param='Самые дорогие')
    assert test_object.city == app.search.get_location_from_first_item_ordinary_list()
import pytest
from fixture.app import Application

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture = Application(browser='chrome', baseurl='https://www.olx.ua/')
    return fixture

@pytest.fixture(autouse="True")
def stop(request):
    request.addfinalizer(fixture.destroy)
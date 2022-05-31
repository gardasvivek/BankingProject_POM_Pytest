from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pytest

from Config.TestData import TestData


@pytest.fixture(params=["Firefox"],scope="class")
def initialize_driver(request):
    if request.param=="Firefox" :
        web_diver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver=web_diver
        web_diver.implicitly_wait(10)


        #web_diver.get(TestData.BaseUrl)
        web_diver.maximize_window()

    yield
    web_diver.close()




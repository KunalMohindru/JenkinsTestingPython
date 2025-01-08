import pytest
from selenium import webdriver
import importlib

@pytest.fixture(scope="function", autouse=True)
def create_Driver(request):

    # the browser value passed in cmd prompt would be retrieved here
    browser=request.config.getoption("browser_name")
    driver=set_BrowserDriver(browser)
    request.cls.driver = driver    

    # the env value passed in cmd prompt would be retrieved here
    reqd_env=request.config.getoption("env")
    config_obj=load_env_config(reqd_env)
    request.cls.config_obj= config_obj

    yield 
    driver.close()
  

@pytest.hookimpl()
def pytest_addoption(parser):
    # it tells the command line to accept a key-value pair with key --brower_name and store it
    parser.addoption(
        "--browser_name", action="store", default="chrome")
    
    parser.addoption(
        "--env", action="store", default="QA")
    

def load_env_config(env):
    # Dynamically import the correct environment config file
    config = importlib.import_module(f'Env_config.{env}_config')
    return config


def set_BrowserDriver(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()

    elif browser=="edge":
        driver=webdriver.Edge()

    elif browser=="headless":
        options_obj = webdriver.ChromeOptions()
        options_obj.add_argument("--headless") 
        driver = webdriver.Chrome(options=options_obj)
    
    driver.maximize_window()
    return driver
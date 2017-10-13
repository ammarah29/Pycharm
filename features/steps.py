from lettuce import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from sys import platform
import time
import os

directory = os.path.dirname(__file__)
if platform == "win32":
    driver_location = os.path.join(directory, '..\chromedriver_win32.exe')
elif platform == "darwin":
    driver_location = os.path.join(directory, '../chromedriver_mac')


@before.all
def setup():
    world.driver = webdriver.Chrome(driver_location)
    homepage = 'http://www.asos.com/'
    world.driver.get(homepage)


@step('I want to order a shirt')
def select_shirts(step):
    hover = ActionChains(world.driver).move_to_element(world.driver.find_element_by_xpath("//span[contains(.,'WOMEN')]"))
    hover.perform()
    shirts = world.driver.find_element_by_xpath("//a[@href='http://www.asos.com/women/tops/t-shirts-vests/cat/?cid=4718']")
    assert EC.presence_of_element_located(shirts)
    shirts.click()


@step('I search for purple t shirts')
def search_purple_tshirts(step):
    world.driver.find_element_by_xpath("//li[@data-name='Purple']").click()
    time.sleep(2)


@step('I should see some purple t shirts')
def assert_purple_tshirts(step):
    assert world.driver.current_url == 'http://www.asos.com/women/tops/t-shirts-vests/cat/?cid=4718&refine=base_colour:8&currentpricerange=0-165&pgesize=36'


@step('I search for yellow t shirts in the Australian store')
def yellow_tshirts_au(step):
    world.driver.find_element_by_xpath("//span[@class='selected-currency']").click()
    time.sleep(2)
    world.driver.find_element_by_xpath("//a[contains(.,'Australia')]").click()
    time.sleep(2)
    world.driver.find_element_by_xpath("//li[@data-name='Yellow']").click()
    time.sleep(2)

@step('I should see some yellow t shirts')
def assert_yellow_tshirts_au(step):
    assert world.driver.current_url == 'http://www.asos.com/au/women/tops/t-shirts-singlets/cat/?cid=4718&refine=base_colour:6&currentpricerange=5-330&pgesize=36'


@step('I choose a yellow t shirt')
def choose_yellow_tshirts_au(step):
    world.driver.find_element_by_xpath(".//*[@id='productlist-results']/div/div[3]/ul/li[1]/a/div[1]").click()


@step('I save it for later')
def save_for_later_yellow_tshirts_au(step):
    world.driver.find_element_by_class_name("save-button-link").click()
    world.driver.find_element_by_xpath(".//*[@id='product-save']/div/a").click()
    time.sleep(3)
    assert world.driver.find_element_by_xpath("//*[@class='save-button-link active animate']")


@step('I add it to my basket')
def save_for_later_yellow_tshirts_au(step):
    world.driver.find_element_by_xpath("//span[contains(.,'Add to bag')]").click()
    assert world.driver.find_element_by_xpath("//span[contains(.,'Please select from the available colour and size options')]")

    world.driver.find_element_by_xpath("//select[@class='required']").click()
    world.driver.find_element_by_xpath("//option[contains(.,'AU 8')]").click()
    world.driver.find_element_by_xpath("//span[contains(.,'Add to bag')]").click()
    time.sleep(2)
    assert world.driver.find_element_by_xpath("//span[contains(.,'(1)')]")


@after.all
def close_browser(step):
    world.driver.quit()
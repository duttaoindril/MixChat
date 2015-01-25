from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium import select
import selenium
#from sys import argv
#script, query, month, day, date = argv
#only if accessing as its own file

url = 'https://www.facebook.com/messages/'

driver = webdriver.Firefox()
driver.get(url)
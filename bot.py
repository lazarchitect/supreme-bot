from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

######################
## CONSTANTS
######################
URL = "https://www.supremenewyork.com/shop/jackets/ztsve421k"

name = "Eddie Lazar"
email = "eddie.lazar@yahoo.com"
tel = "7325338909"
address = "48 Sutton Drive"
zipcode = "07726"
city = "Manalapan"
state = "NJ"

ccnum = "1234555567890000"
cvv = "800"
ccmonth = "11"
ccyear = "2022"

######################
## BOT CODE
######################
driver = webdriver.Chrome()

driver.get(URL) #GET TO JACKET PAGE

driver.find_element_by_name("commit").click() #ADD TO CART
driver.find_element_by_class_name("checkout").click() #GO TO CHECKOUT SCREEN
driver.find_element_by_xpath("//input[@id='order_billing_name']").send_keys(name)#enter name
driver.find_element_by_xpath("//input[@id='order_email']").send_keys(email)#enter email
driver.find_element_by_xpath("//input[@id='order_tel']").click()#prepare telephone number form
driver.find_element_by_xpath("//input[@id='order_tel']").send_keys(tel)#enter telephone number
driver.find_element_by_xpath("//input[@id='bo']").send_keys(address)#enter address
driver.find_element_by_xpath("//input[@id='order_billing_zip']").send_keys(zipcode)#enter zipcode. also auto inserts city
Select(driver.find_element_by_xpath("//select[@id='order_billing_state']")).select_by_value("NJ") #select state from dropdown

driver.find_element_by_xpath("//input[@id='nnaerb']").send_keys(ccnum)#enter ccnum
driver.find_element_by_xpath("//input[@id='orcer']").send_keys(cvv)#enter cvv
Select(driver.find_element_by_xpath("//select[@id='credit_card_month']")).select_by_value(ccmonth) #select credit card month from dropdown
Select(driver.find_element_by_xpath("//select[@id='credit_card_year']")).select_by_value(ccyear) #select state from dropdown
driver.find_element_by_xpath("//label/div/ins[@class='iCheck-helper']").click()#check off T&C box









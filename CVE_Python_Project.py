# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
import datetime
current_date = datetime.datetime.now()
current_year = current_date.year

def input_validation():
    cve_input = input("I am looking for CVE-")
    numbers = []
    numbers_str = []
    if "-" not in cve_input or cve_input.count("-") > 1:
        print("CVE format should be like CVE-YYYY-NNNN\nTry a new one")
        return input_validation()
    for iy in range(2):
        if cve_input.split("-")[iy] == "":
            print("CVE format should be like CVE-YYYY-NNNN\nTry a new one")
            return input_validation()
    for i in range(2):
        try:
            numbers_str.append(cve_input.split("-")[i])
            numbers.append(int(cve_input.split("-")[i]))
        except ValueError:
            print("An ID should contain only digits\nTry a new one")
            return input_validation()
    length = len(numbers_str)
    if length != 2:
        print("We just need 2 numbers in ID\nTry a new one")
        return input_validation()
    if numbers[0] >= current_year:
        print("Year is far from us\nEnter id again")
        return input_validation()
    elif numbers[0] <= 1999:
        print("There is no CVEs before 1999 ;)\nTry a new one")
        return input_validation()
    if len(numbers_str[1]) < 4:
        print("ID must be 4 or more digits!")
        return input_validation()
    if numbers[1] == 0:
        print("ID cannot contain all zeros")
        return input_validation()











input_validation()





















































# from selenium.webdriver.chrome.service import Service

# service = Service(executable_path="")



# browser = webdriver.Firefox()
# url = "https://www.exploit-db.com/"
#
# browser.get(url)
#
# info1 = browser.find_element(By.CLASS_NAME, "col-sm-12")
#
# print(info1)
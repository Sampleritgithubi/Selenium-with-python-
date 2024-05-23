#Webtable
#there are two types of webtable
"""
Webtable
webtable is a collection of rows and coloumns for a webtable data is stored
in cells table are used not only to store data but also arrange web pages

#1)static table- where values under table are constant
#2) dynamic table- values inside cell are changing(dynamic)
# seb site used https://testautomationpractice.blogspot.com/
where,
tr=table row
th-table header
td-table data
#Demo-
1. Count no of rows and coloumn
2. read a specific row and coloumn
3. read all the rows and coloumn data
4. read all based on condition (list books name whose author is mukesh

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

#Fine no of rows and couloumn
#Rows
#xpath -//table[@name='BookTable']/tbody/tr OR  //table[@name='BookTable']//tr
allrows_tr=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")

#print(len(allrows_tr))
#............or............#
allrows_tr=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))



#Print all couloumn
#Xpath- //table[@name='BookTable']//th
allcoloumns_th=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")

#print(len(allcoloumns_th))

#------------------OR------------------
allcoloumns_th=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

#2) Read sepecific row and coloumn data
#Row or coloumn no need to write in Xpath

data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)



#Read all rows and coloumn data
#using looping statement
# 2 loops we will use  one for row and one for coloumn
"""
print("Printing all rows and coloumn data....")

#range we use indexing which starts from 0,1,2,3
for r in range(2,allrows_tr+1): #allrows_tr taken from above part-1 o/p

    for c in range(1,allcoloumns_th+1): #allcoloumns_th taken from above part-1 o/p
        data2=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text


        #use string format before and after- tr"+str[r]+"/td"+str[c]
        print(data2)  # will print data
        print()   #space will be created b/w table data

        print(data2,end='           ') #will print in tabular form
        print()
        
        """
#4) Read data based on condition list books name whose author is mukesh in table
#muskesh is present on 2nd coloum in 2nd and 4th row
#use for loop 1st line is header
for r in range(2,allrows_tr+1):
    # xpath- //table[@name='BookTable']/tbody/tr[2]/td[2]  replace with strings as well
    #with +str+
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author=="Mukesh":
        #Book xpath- // table[ @ name = 'BookTable'] / tbody / tr[2] / td[1] #rplace with str
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]")

        print(bookname,"     ",author)
price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text

print(bookname,"",author,"",price)


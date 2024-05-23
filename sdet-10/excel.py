import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By


excel_path = "C:/Users/Admin/Desktop/prashanth/read data.xlsx"
workbook = openpyxl.load_workbook(excel_path)
sheet = workbook.active


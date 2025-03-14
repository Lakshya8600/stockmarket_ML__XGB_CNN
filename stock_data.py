# save file for each company's stock data in csv format of 5 years. stock_data folder


import yfinance
import pandas as pd
import csv
import os
import re

folder_path = "C:/Code/ml/stock_data_csvs"
with open('CompanyNames.csv',mode='r',newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        company_name = row[0].strip()
        # print (company_name)
        data = yfinance.Ticker(company_name)
        # print(data.history(period="5y"))
        df = data.history(period="5y")
        company_name_ = company_name.replace(".NS","")
        company_name_ = re.sub(r'[^\w]','_',company_name_)
        file_path = os.path.join(folder_path, f"{company_name_}.csv")
        df.to_csv(file_path,index=False)
        
# save file for each company's stock data in csv format of 5 years. stock_data folder


import yfinance
import pandas as pd
import csv
import os
import re

<<<<<<< HEAD
folder_path = "stock_data_csvs"
=======
# storing stock data to stock_data_csvs
folder_path = "C:/Code/ml/stock_data_csvs"
>>>>>>> d97a453d0fed16d63f11c20338a1fa11389366a6
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
        for i in range(len(df)):
            df.iloc[i,5] = (df.iloc[i,4] - df.iloc[i,1])/df.iloc[i,1]
            if df.iloc[i,5]>= 0.03 :
                df.iloc[i,5] = 1
            elif df.iloc[i,5] <= -0.03:
                df.iloc[i,5] = -1
            else:
                df.iloc[i,5] = 0
       
        df = df.iloc[:,5]
        df.to_csv(file_path)

# TO EXPORT ALL data in csv         
# import yfinance
# import pandas as pd
# import csv
# import os
# import re

# folder_path = "stock_data_csvs"
# with open('CompanyNames.csv',mode='r',newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         company_name = row[0].strip()
#         # print (company_name)
#         data = yfinance.Ticker(company_name)
#         # print(data.history(period="5y"))
#         df = data.history(period="5y")
#         company_name_ = company_name.replace(".NS","")
#         company_name_ = re.sub(r'[^\w]','_',company_name_)
#         file_path = os.path.join(folder_path, f"{company_name_}.csv")
#         df.to_csv(file_path)
        

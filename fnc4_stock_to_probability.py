# # function 4:- takes stock name, date list and returns stock and probability per stock name

# import pandas as pd
# from datetime import datetime
# import os

# base_dir = os.path.dirname(__file__)
# # convert headline_sim list to a pandas dataframe

# def stp(stock,datelist):
#     df = pd.DataFrame(datelist)
#     for i in range(len(df)):
#         # date_u = df.iloc[i,0] #unformatted date
#         # date_obj = datetime.strptime(str(date_u), "%Y%m%d")
#         date_u = df.iloc[i, 0]
#         if isinstance(date_u, str) and " " in date_u:  
#             date_obj = datetime.fromisoformat(date_u.split()[0]) 
#         else:
#             date_obj = datetime.strptime(str(date_u), "%Y%m%d") 
#         date = date_obj.strftime("%Y-%m-%d") #formatted date

#         path = os.path.join(base_dir, "indicator_data_csvs", f"{stock}_indicator.csv")

#         # Read CSV
#         df_true = pd.read_csv(path)
#         df = df_true.copy(deep=True)
#         # print(df.head())
#         container = []
#         df["date_only"] = pd.to_datetime(df['Date']).dt.date #gives date of Date column excluding time as a date object
        
#         for j in df["date_only"]:
#             if date == j:
#                 container.append(df.iloc[j,2])
#         print(container)
        
# datelist = [20230117,20220113,20240113]
# stp("HDFCBANK", datelist)

import pandas as pd
from datetime import datetime
import os

base_dir = os.path.dirname(__file__)

def stp(stock, datelist):
    df_dates = pd.DataFrame(datelist, columns=['date_raw'])

    # Convert integer dates to datetime.date objects
    df_dates["formatted_date"] = df_dates["date_raw"].astype(str).apply(lambda x: datetime.strptime(x, "%Y%m%d").date())

    path = os.path.join(base_dir, "indicator_data_csvs", f"{stock}_indicator.csv")

    # Read CSV
    df = pd.read_csv(path)

    # Debug: Print column names
    # print("CSV Column Names:", df.columns)

    # Clean column names (in case of extra spaces)
    df.columns = df.columns.str.strip()

    # Convert 'Date' column to date-only format
    df["date_only"] = pd.to_datetime(df['Date']).dt.date

    # Debug: Print unique dates from the CSV
    # print("Unique dates in CSV:", df["date_only"].unique())

    results = []  # Store results

    for date_obj in df_dates["formatted_date"]:
        # print(f"\nChecking for date: {date_obj}")

        # Filter the DataFrame for the specific date
        filtered_row = df[df["date_only"] == date_obj]

        if not filtered_row.empty:
            # Debug: Print matched row
            # print("Matched row:", filtered_row)

            # Get the first matched value from the "indicator" column
            indicator_value = int(filtered_row["indicator"].values[0])  # Convert np.int64 to int
            results.append(indicator_value)
        else:
            results.append(None)  # Append None if date not found

    print("\nFinal Results:", results)  # Output the list of indicator values

# Example usage
datelist = [20200313, 20220912, 20220912]
stp("HDFCBANK", datelist)



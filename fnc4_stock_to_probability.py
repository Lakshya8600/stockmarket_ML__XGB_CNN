# # function 4:- takes stock name, date list and returns stock and probability per stock name

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
    sum = 0
    nume = 0
    for i in range(len(results)):
        sum = sum+results[i]
    if sum>0:
        for j in range(len(results)):
            if results[j]==1:
                nume = nume+results[j]
    elif sum<0:
        for k in range(len(results)):
            if results[k]==(-1):
                nume = nume+results[k] 
    else:
        nume = 0
    
    probability = nume/(len(results)) 
    return probability 

# # Example usage
# datelist = [20200313, 20220912, 20220912]
# print(stp("HDFCBANK", datelist))



# FUNCTION-4:- 
# INPUT:- stock name, datelist(of dates for which the target headline matched with the past news' headline with desired similarity score)
# OUTPUT:- probability of stock increase or decrease based on the given headline


def stp(stock, datelist):
    import os
    import pandas as pd

    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "indicator_data_csvs", f"{stock}_indicator.csv")

    if not os.path.exists(path):
        return None  # Return None if file doesn't exist

    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df["date_only"] = pd.to_datetime(df["Date"], errors='coerce').dt.date
    df = df.dropna(subset=["date_only"])

    results = []
    for date_obj in datelist:
        filtered_row = df[df["date_only"] == date_obj]
        results.append(int(filtered_row["indicator"].values[0]) if not filtered_row.empty else None)

    if not any(results):  # If all values are None or empty
        return 0

    sum_results = sum(filter(None, results))
    nume = sum(1 for v in results if v == 1) if sum_results > 0 else sum(-1 for v in results if v == -1)

    return nume / len(results)

# # Example usage
# datelist = [20200313, 20220912, 20220912]
# print(stp("HDFCBANK", datelist))



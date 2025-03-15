from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np 
import os
from datetime import datetime, timedelta
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Configure WebDriver options
options = Options()
options.add_argument("--headless")  # Run without opening a browser
options.add_argument("--disable-gpu")  
options.add_argument("--window-size=1920,1080")  
options.add_argument("--no-sandbox")  
options.add_argument("--disable-dev-shm-usage")  

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

today = datetime.today()

for b in range(42442,45730):
# b = 42442
# b = 45729 gives date = 13 march 2025
    try:
        date = today - timedelta(days=45729-b+1)
        year = date.year
        month = date.month
        day = date.day
    # print(date.strftime("%Y%m%d")) 
    # print(month)  
        url = f"https://economictimes.indiatimes.com/archivelist/year-{year},month-{month},starttime-{b}.cms"
        driver.get(url)
        

        # Wait for the page to load completely
        # time.sleep(3)

        # --------------------

        html = driver.page_source  # Get page source
        soup = BeautifulSoup(html, "html.parser")

        # Find the <ul> with class "content"
        ul_tag = soup.find("ul", class_="content")

        # Extract all <li> items inside the <ul>

        list_items = [li.get_text(strip=True).split() for li in ul_tag.find_all("li")]  # List of lists
        numpy_array = np.array(list_items, dtype=object)  # Convert to NumPy 2D array
        # print(numpy_array)

        # # Extract all text
        # text = soup.get_text()

        # # Extract all links
        # links = [a["href"] for a in soup.find_all("a", href=True)]

        # # Extract all images
        # images = [img["src"] for img in soup.find_all("img", src=True)]

        # # Extract all table data
        # tables = soup.find_all("table")

        # # Print results
        # print("Text:\n", text)
        # print("\nLinks:\n", links)
        # print("\nImages:\n", images)
        # print("\nTables:\n", tables)

        folder_path = "C:/Users/saira/OneDrive/Desktop/Model-1.0/data/" 
        os.makedirs(folder_path, exist_ok=True)

        date_format = date.strftime("%Y%m%d")
        file_path = os.path.join(folder_path, f"{date_format}.csv")

        np.savetxt(file_path, numpy_array, delimiter=",", fmt="%s")
    except:
        file_path = os.path.join(folder_path, f"Not found{date_format}.csv")
        np.savetxt(file_path, numpy_array, delimiter=",", fmt="%s")
        


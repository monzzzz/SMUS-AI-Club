import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def webpage_info():
    print("Exploring...")
    json_path = "smus_page.json"

    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    url_list = [page["url"] for page in data["organic_results"]]
    
    all_data = []

    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            paragraphs = soup.find_all('p')
            
            page_content = " ".join([p.get_text() for p in paragraphs]) 
            all_data.append([url, page_content]) 

        else:
            print(f"Failed to retrieve the page: {url}. Status code: {response.status_code}")

    df = pd.DataFrame(all_data, columns=["URL", "Page Content"])

    df.to_excel('smus_page.xlsx', index=False)
    print("All page content saved to 'webpages_content_combined.xlsx'")

def xlsx_to_csv():
    excel_file = 'smus_page.xlsx'  
    df = pd.read_excel(excel_file, engine='openpyxl')
    csv_file = 'smus_page.csv'
    df.to_csv(csv_file, index=False)

webpage_info()






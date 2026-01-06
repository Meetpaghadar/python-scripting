import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes"

# This header makes the website think you are using the Chrome browser
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" 
}

# 1. Fetch the content manually
response = requests.get(url, headers=headers)

# 2. Check if it worked (200 means OK)
if response.status_code == 200:
    # 3. Pass the text content to Pandas
    # Use StringIO to make the string look like a file to Pandas
    data = StringIO(response.text)
    
    # If you were using read_html:
    dfs = pd.read_html(data)
    print(dfs[0].head()) # Print first few rows of the first table
    
    # If you were using read_csv:
    # df = pd.read_csv(data)
    # print(df.head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# import pandas as pd
# simpsons=pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes")
# len(simpsons)

print(len(dfs))
# %%
import requests
from bs4 import BeautifulSoup
# %%
# Specifying the URL
url = "https://edition.cnn.com/2023/12/06/politics/takeaways-republican-debate"
# Sending a request to the webpage
response = requests.get(url)
# Ensure the request was successful
if response.status_code != 200:
    raise Exception(f"Failed to fetch webpage: Status code {response.status_code}")

# %%
# Parsing  HTML content
soup = BeautifulSoup(response.content, "html.parser")
# Scrape section using HTML tags
description_html = soup.find_all("p")
texts = [text.get_text().strip() for text in description_html]
text = "\n".join(texts)

print(text)

# %%

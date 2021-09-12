import json
from bs4 import BeautifulSoup
import requests

site_url = 'https://img.webmatrices.com/'
response = requests.get(site_url)
source = response.text

soup = BeautifulSoup(source, 'html.parser')

gallery_elements = soup.find_all('div', class_ = 'gallery')
# or .find_all('div', {'class': 'gallery'})

gallery_data = {}
for index, gallery_element in enumerate(gallery_elements):
   image = gallery_element.find('img')
   image_source = image['src']
   image_alt = image['alt']
   # for description
   description = gallery_element.find('div', class_="desc")
   # within 
   gallery_data.update({
      index: {
         'source': image_source,
         'alt': image_alt,
         'description': description.text
         }
      })

gallery_data = json.dumps(gallery_data, indent=4)


print(gallery_data)
   

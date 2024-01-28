import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

class Account:
    def __init__(self, account_id: str):
      self.id = account_id
      self.status = {
          'total': 0,
          'active': 0,
          'fault': 0,
          'recovery': 0,
      }
      self.last_check_time = 'not yet'
      self.url: str = pre_url + self.id
      self.update_status()
    
    def update_status(self):
        
        def get_innertext_by_css_selector(soup: bs, selector: str) -> str:
            tags = soup.select(selector)
            firstTag = tags[0]
            firstTagStr: str = firstTag.text
            return firstTagStr
        
        def get_number_only(string: str) -> int:
            numbers: [str] = [word for word in string if word.isdigit()]
            number: str = ''.join(numbers)
            return int(number) 
        
        html = requests.get(self.url).text
        soup = bs(html, 'lxml')
        
        self.status['total'] = get_number_only(get_innertext_by_css_selector(soup, '.text-xs.text-gray-800.text-right > span:first-child'))
        self.status['active'] = get_number_only(get_innertext_by_css_selector(soup, '.text-green-600'))
        self.status['fault'] = get_number_only(get_innertext_by_css_selector(soup, '.text-red-700'))
        self.status['recovery'] = get_number_only(get_innertext_by_css_selector(soup, '.text-yellow-500'))
        
        curr_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.last_check_time = curr_timestamp
        

pre_url = 'https://filfox.info/ko/address/'
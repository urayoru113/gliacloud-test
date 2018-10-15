import requests
import sys
import json
from bs4 import BeautifulSoup

def print_zh_TW(text):
    print(text.encode(sys.stdin.encoding, 'replace').decode(sys.stdin.encoding))

def fetch(url):
    res = requests.get(url, cookies={'over18':'1'});
    return res;

def parse_page(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.find_all('div', class_='title')
    urls = [title.a['href'] for title in titles]
    return urls 
def parse_detail(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    return [
        soup.find_all('span', class_='article-meta-tag'),
        soup.find_all('span', class_='article-meta-value'),
        soup.find('div', id='main-container')
    ]
if __name__ == '__main__':
    authority = 'https://www.ptt.cc'
    url = authority + '/bbs/Gossiping/M.1539424002.A.474.html';
    url = authority + '/bbs/Gossiping'
    res = fetch(url);
    urls = parse_page(res)
    for i, url in enumerate(urls):
        res = fetch(authority + url)
        meta = parse_detail(res)
        data = {}    
        for tag, value in zip(meta[0], meta[1]):
            data[tag.text] = value.text
        data['content'] = meta[2].text
        with open('PTT' + str(i) + '.json', 'w') as f:
            formate_json = json.dumps(data, ensure_ascii=False)
            f.write(formate_json)

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

tickertape_url = "https://www.tickertape.in/stocks/"
tickers = ['PNBK','MRF','RAIV','NTPC']
news_headlines = {}

for ticker in tickers:
    url = tickertape_url + ticker
    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    html = BeautifulSoup(response, 'html.parser')

    news_tab = html.find(id='news-tab')
    if news_tab:
        headlines = [headline.text for headline in news_tab.find_all(
            'span', class_='jsx-1669302504 text-primary headline mb8 heading')]
        news_headlines[ticker] = headlines

print(news_headlines)

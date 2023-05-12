from bs4 import BeautifulSoup
import pandas as pd

with open('ex5-10.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
    data = []
    for tr in soup.select('tr'):
        tds = tr.select('td')
        if len(tds) == 3:
            name = tds[0].text
            score1, score2 = map(int, [tds[1].text, tds[2].text])
            data.append([name, score1, score2])

    df = pd.DataFrame(data, columns=['이름', '국어', '영어']).set_index('이름')
    print(df)

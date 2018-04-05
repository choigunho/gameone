from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import db_test

def collect_data(bs):

    scoreList = bs.find_all('span', {'class': 'score'})

    item = []
    for score in scoreList:
        item.append(score.getText())

    # print(item)


    # db 입력
    db_test.insert_data(item)


if __name__ == "__main__":

    url = "http://www.gameone.kr/locker/record/main?group_code=08F4B5EF9908AC2BA3EA4A51EA578FA1&club_idx=997"

    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        bs = BeautifulSoup(html.read(), 'html.parser')
        data = collect_data(bs)
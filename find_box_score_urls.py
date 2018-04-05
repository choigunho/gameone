import urllib.request
from bs4 import BeautifulSoup

def find_box_score_urls(season, club_idx, game_type):
    url_list = []

    url = "http://www.gameone.kr/club/info/schedule/result?season="+str(season)+"&club_idx="+str(club_idx)+"&game_type="+str(game_type)
    req = urllib.request.Request(url);
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data)

    l = bs.find_all('a')

    idx = 0
    for s in l:
        try:
            prop = s.get('class')
            # print(prop)
            if prop != None and prop[0] == "simbtn":
                # print("%s" % (s.get('href')))
                url_list.append((s.get('href')))
        except UnicodeEncodeError:
            print("Errror : %d" % (idx))
        finally:
            idx += 1
    return url_list



if __name__ == "__main__":

    box_score_urls = find_box_score_urls(2007, 997, 5)
    print(box_score_urls)


import json

import requests
from bs4 import BeautifulSoup


def go(st):
    if st is None:
        return ""
    else:
        if st:
            return str(st).replace('\n', '')
        else:
            return "undefind"


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
mew = requests.get('https://mzh.moegirl.org.cn/Phigros/%E8%B0%B1%E9%9D%A2%E4%BF%A1%E6%81%AF', headers=header)
soup = BeautifulSoup(mew.text)
ul_data = soup.find_all('table', class_='wikitable')
items = (ul_data[0].find_all("td"))

data_list = {}
for idx, item in enumerate(ul_data):

    if idx:
        tds = item.find_all('td')
        song = item.th.string
        illustration = (tds[0].a.img.get('src'))
        chapter = item.find('td', text="所属章节").find_next("td").string
        bpm = item.find('td', text="BPM").find_next("td").string
        composer = item.find('td', text="曲师").find_next("td").string
        length = item.find('td', text="长度").find_next("td").string
        illustrator = item.find('td', text="画师").find_next("td").string
        chart = {}
        if not item.find('td', text="EZ") is None:
            ez_level = item.find('td', text="EZ").find_next("td").string
            ez_difficulty = ez_level.find_next("td").string
            ez_combo = ez_difficulty.find_next("td").string
            ez_charter = ez_combo.find_next("td").string
            chart["EZ"] = {
                              "level": go(ez_level),
                              "difficulty": go(ez_difficulty),
                              "combo": go(ez_combo),
                              "charter": go(ez_charter)

                          },
        else:
            ez_level = 0
            ez_difficulty = 0
            ez_combo = 0
            ez_charter = 0

        if not item.find('td', text="HD") is None:
            hd_level = item.find('td', text="HD").find_next("td").string
            hd_difficulty = hd_level.find_next("td").string
            hd_combo = hd_difficulty.find_next("td").string
            hd_charter = hd_combo.find_next("td").string
            chart["HD"] = {
                              "level": go(hd_level),
                              "difficulty": go(hd_difficulty),
                              "combo": go(hd_combo),
                              "charter": go(hd_charter)
                          },
        else:
            hd_level = 0
            hd_difficulty = 0
            hd_combo = 0
            hd_charter = 0

        if not item.find('td', text="IN") is None:
            in_level = item.find('td', text="IN").find_next("td").string
            in_difficulty = in_level.find_next("td").string
            in_combo = in_difficulty.find_next("td").string
            in_charter = in_combo.find_next("td").string
            chart["IN"] = {
                              "level": go(in_level),
                              "difficulty": go(in_difficulty),
                              "combo": go(in_combo),
                              "charter": go(in_charter),
                          },

        else:
            in_level = 0
            in_difficulty = 0
            in_combo = 0
            in_charter = 0

        if not item.find('td', text="Legacy") is None:
            lc_level = item.find('td', text="Legacy").find_next("td").string
            lc_difficulty = lc_level.find_next("td").string
            lc_combo = lc_difficulty.find_next("td").string
            lc_charter = lc_combo.find_next("td").string  # if not lc_charter is None else "15"
            chart["Legacy"] = {
                                  "level": go(lc_level),
                                  "difficulty": go(lc_difficulty),
                                  "combo": go(lc_combo),
                                  "charter": go(lc_charter),
                              },

        else:
            lc_level = 0
            lc_difficulty = 0
            lc_combo = 0
            lc_charter = 0
        if not item.find('td', text="AT") is None:
            at_level = item.find('td', text="AT").find_next("td").string
            at_difficulty = at_level.find_next("td").string
            at_combo = at_difficulty.find_next("td").string
            at_charter = at_combo.find_next("td").string
            chart["AT"] = {
                              "level": go(at_level),
                              "difficulty": go(at_difficulty),
                              "combo": go(at_combo),
                              "charter": go(at_charter)

                          },
        else:
            at_level = 0
            at_difficulty = 0
            at_combo = 0
            at_charter = 0

        print(f"写出了{go(composer)}的作品{go(song)}")
        data_list[go(song) + "_" + go(composer)] = {
                                                       "song": go(song),
                                                       "illustration": go(illustration),
                                                       "chapter": go(chapter),
                                                       "bpm": go(bpm),
                                                       "composer": go(composer),
                                                       "length": go(length),
                                                       "illustrator": go(illustrator),
                                                       "chart": chart
                                                   },
data = json.dumps(data_list, sort_keys=True, indent=4, separators=(',', ':'))

with open("Phigros.json", 'w+') as f:  
    print("写出了数据")
    f.write(data)

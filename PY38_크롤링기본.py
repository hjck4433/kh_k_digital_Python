import requests # 서버로부터 정보를 요청해서 가져오기, get방식으로 가져 올 예정
from bs4 import BeautifulSoup as bs # html parser
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# html = requests.get(url).text
# #print(html)
# soup = bs(html, "html.parser")
# print(soup)

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# http Get 요청
res = requests.get(url).text
# HTML 파싱
soup = bs(res,"html.parser")
#print(soup)

for loc in soup.select("location") :
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-" * 20)
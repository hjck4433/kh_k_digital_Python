from bs4 import BeautifulSoup

# HTML 문서
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <a href="https://www.example.com">Link</a>
    <a href="https://www.example.com">Link2</a>
  </body>
</html>
'''

# HTML 문서를 파싱하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')
#타이틀 태그 검색
# title_tag = soup.title
# print(title_tag)
# # 클래스가 "content"인 div태그 검색
# div_tag = soup.select("div.content")
# print(div_tag)
#
# for div in div_tag :
#     print(div.text)

#href 속성이 있는 모든 a 태그 검색
a_tags = soup.findAll("a", href=True)

for a_tag in a_tags:
    print(a_tag)


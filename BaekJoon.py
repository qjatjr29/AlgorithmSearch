import requests
from bs4 import BeautifulSoup


BaekJoon_Algorithm = requests.get("https://www.acmicpc.net/problem/tags")
# print(BaekJoon_Algoritm.text)
BaekJoon_Soup = BeautifulSoup(BaekJoon_Algorithm.text, "html.parser")

# 클래스 명이 table-responsive인 div 태그 반환.
Algorithm_page = BaekJoon_Soup.find("div", {"class": "table-responsive"})
# div 태그 들에서 a태그 반환
Algorithm_type = Algorithm_page.find_all('a')

Algorithm_name = []
for name in Algorithm_type:
    Algorithm_name.append(name.string)

print(Algorithm_name)

# 지금 까지 알고리즘 종류 ( 한글, 영어 ) 리스트형식으로 저장
# 내가 찾고 싶은 것을 검색해서 리스트에서 찾아 그 링크로 들어가기.
# 그후 거기에 있는 모든페이지의 문제 추출.


# 바꿔야함 함수.
def get_Algorithm(name):
    url = "https://www.acmicpc.net/problem/tags"
    return name

from bs4 import BeautifulSoup
import requests
import json

URL = "https://codeup.kr/ranklist_1.php?school=619"

def rankingApi():
	ranking = []
	res = requests.get(URL)
	html = res.text
	soup = BeautifulSoup(html,'html.parser')

	for i in range(1,51):
		rank = int(soup.select_one(f"#ranklist > tbody > tr:nth-child({i}) > td:nth-child({1})").text)
		id = soup.select_one(f"#ranklist > tbody > tr:nth-child({i}) > td:nth-child({2})").text
		username = soup.select_one(f"#ranklist > tbody > tr:nth-child({i}) > td:nth-child({3})").text
		solved = int(soup.select_one(f"#ranklist > tbody > tr:nth-child({i}) > td:nth-child({4})").text)
		submit = int(soup.select_one(f"#ranklist > tbody > tr:nth-child({i}) > td:nth-child({5})").text)

		ranking.append(
			{
				"rank" : rank,
				"id" : id,
				"username" : username,
				"solved" : solved,
				"submit" : submit
			}
		)
	
	return json.dumps(ranking,ensure_ascii=False)

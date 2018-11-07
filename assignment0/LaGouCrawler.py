import requests
from bs4 import BeautifulSoup  

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

for i in range(1,30+1):

	url = 'https://www.lagou.com/zhaopin/Python/' + str(i)
	
	r = requests.get(url, headers=header)

	soup = BeautifulSoup(r.text, 'html.parser')

	# 发布时间
	format_time = soup.select(".position .p_top .format-time")  
	# 职位
	position = soup.select(".position .p_top .position_link h3")
	# 地点
	location = soup.select(".position .p_top .position_link .add em")
	# 薪水
	salary = soup.select(".position .p_bot .li_b_l span")
	# 经验学历
	exp = soup.select(".position .p_bot .li_b_l")
	# 公司名
	company_name = soup.select(".list_item_top .company .company_name a")
	# 企业状况
	industry = soup.select(".con_list_item .list_item_top .company .industry")
	# 公司标签
	label1 = soup.select(".list_item_bot .li_b_l")
	label2 = soup.select(".list_item_bot .li_b_r")

	with open("saved.csv", 'a') as f:
		for i in range(len(format_time)):
			f.write(
				format_time[i].text.replace("\n", "") + "," + position[i].text.replace("\n", "") + "," + location[i].text.replace("\n", "") + ","
				 + salary[i].text + ","+ exp[i].text.strip().replace(salary[i].text, "").replace("\n", "") + "," +
				company_name[i].text.replace("\n", "") + "," + industry[i].text.strip().replace("\n", "") + "," +
				label1[i].text.strip().replace("\n", "").replace("“", "\"").replace("”", "\"") + "," +
				label2[i].text.replace("\n", "").replace("“", "\"").replace("”", "\"") + "\n")
	f.close()

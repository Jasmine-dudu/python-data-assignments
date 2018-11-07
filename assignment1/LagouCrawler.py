import requests
from bs4 import BeautifulSoup
import time

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

for i in range(1, 10 + 1):
    
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

	with open("saved.csv", 'ab') as f:
		for j in range(len(format_time)):
			f.write(
				(format_time[j].text.replace("\n", "") + "," + position[j].text.replace("\n", "") + "," + location[j].text.replace("\n", "") + ","
				 + salary[j].text + ","+ exp[j].text.strip().replace(salary[j].text, "").replace("\n", "") + "," +
				company_name[j].text.replace("\n", "") + "," + industry[j].text.strip().replace("\n", "") + "\t" +
				label1[j].text.strip().replace("\n", "").replace("“", "\"").replace("”", "\"") + "," +
				label2[j].text.replace("\n", "").replace("“", "\"").replace("”", "\"") + "\n").encode('gbk'))
		f.close()
	time.sleep(10 + i)

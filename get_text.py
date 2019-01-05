import requests
from bs4 import BeautifulSoup
import time
import re 

###运行次文件会创建三个txt
###reviews_date.txt 短评日期
###reviews_data.txt 短评内容
###score.txt 评分占比
###在下面修改配置
url = 'https://movie.douban.com/subject/24723061/' #电影网址
num = 1000 # 想要获取短评的数量

def get_text(url):
	k = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	r = requests.get(url,headers = k)
	r.encoding= 'utf-8'
	return r.text

def get_score(soup):
	score_list = []
	score_dict = {}
	all_score = soup.find('div',{'class' :"ratings-on-weight"}).find_all('span')
	for score in all_score:
		score_list.append( score.text.strip() )
	for i in range(0,len(score_list),2):
		score_dict[ score_list[i] ] = score_list[i+1]
	return score_dict

def get_reviews(url, num ):
	reviews = []
	#/comments?start=0&limit=20&sort=new_score&status=P
	text = get_text(url)
	pages = re.findall('P">(.*?)<' ,str(text),re.S)[0]
	pages =  int(re.findall('\d+',str(pages))[0])
	pages = int(min(pages, num )) #最小获取量·

	for page in range(0,pages ,20 ):
		url1 = url + 'comments?start=' + str(page) + '&limit=20&sort=new_score&status=P'
		text = get_text(url1)
		soup = BeautifulSoup(text,'html.parser')
		data = soup.find_all('div', {'class' : "comment-item"})
		for da in data:
			date = da.find('span',{'class' : "comment-time "}).text.strip()
			connect = da.find('span',{'class':'short'}).text.strip()
			reviews.append( [ date,connect ] )

		print('短评已获取'+ str(page*100 / pages)[:5] + '%' )
		time.sleep(2)
	print('短评获取完成')
	return reviews

def main(url,num):
	url = url + '/' if url[-1] != '/' else url
	text = get_text(url)
	soup = BeautifulSoup(text,'html.parser')
	###score
	score_dict = get_score(soup)
	with open('score.txt','w',encoding='utf-8') as f:
		for _ in score_dict:
			f.write(str(_) + ' ' + str(score_dict[_]) + '\n')
	###reviews
	reviews = get_reviews(url, num) #短评网址不一样
	with open('reviews_date.txt','a+',encoding='utf-8') as f_date:
		with open('reviews_data.txt','a+',encoding='utf-8') as f_data:
			for review in reviews:
				f_date.write( str(review[0])+ ' ' )
				f_data.write( str(review[1])+ ' ' )

main(url,num)
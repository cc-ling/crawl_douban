from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import jieba 
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   #解决中文乱码问题

with open('reviews_data.txt', 'r' ,encoding='utf-8') as f:
	text = f.read()
with open('score.txt', 'r' ,encoding='utf-8') as f:
	score = f.read().split()
with open('reviews_date.txt', 'r' ,encoding='utf-8') as f:
	date = f.read().split()

def word_cloud(text):
	###词云
	text = " ".join(jieba.cut(text))
	wordcloud = WordCloud(width=600, height=350, #画布长、宽，默认（400,200）像素
		max_font_size=66,
		font_path = 'msyh.ttc' ,
		stopwords= ('魁拔',  ), #设置需要屏蔽的词
		max_words=200,#显示的词的最大个数
		).generate(text)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig('短评词云.png')
	plt.show()

def count_graph(text):
	text = " ".join(jieba.cut(text))
	###高频词汇统计条形图
	counts = {}
	for word in text.split():
	    if len(word) == 1:
	        continue
	    else:
	        counts[word] = counts.get(word,0) + 1
	items = list(counts.items())
	items.sort(key=lambda x:x[1], reverse=True) 

	counts_num = []; counts_data = []
	for item in items:
		counts_num.append( item[0] )
		counts_data.append(item[1] )

	fig1 = plt.figure(2)
	rects =plt.bar( counts_num[:15] , counts_data[:15]  )  #只显示前十五个
	plt.title('高频词汇统计')
	plt.savefig('高频词汇统计.png')
	plt.show()


def score_pit(score):
	labels = []; sizes = []
	for i in range(0,len(score),2):
		labels.append(score[i])
		sizes.append( eval(score[i][:-1]) )

	plt.pie(sizes,labels=labels,startangle=150,
		autopct="%1.1f%%", #设置圆里面文本

		)
	plt.title("评分分布统计饼图")
	plt.savefig('评分分布统计饼图.png')
	plt.show()

def date_graph(date):
	counts = {}
	for word in date:
	    if len(word) == 1:
	        continue
	    else:
	        counts[word] = counts.get(word,0) + 1
	items = list(counts.items())
	items.sort(key=lambda x:x[0], reverse=False) 

	counts_num = []; counts_date = []
	for item in items:
		counts_num.append( item[0] )
		counts_date.append(item[1] )

	#设置画布像素
	plt.figure(figsize=(8,6))
	#给X、Y轴赋值
	plt.plot(counts_num,counts_date  ,"r",linewidth=1)
	plt.xticks(range(0,len(counts_date),15)) #x轴刻度
	#设置X、Y轴名称
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.title('日期与评论数量')
	plt.savefig('日期分布条形图.png')
	plt.show()

def main(text,score):
	word_cloud(text)
	count_graph(text)
	score_pit(score)
	date_graph(date)

main(text,score)


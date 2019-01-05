# crawl_douban
爬取豆瓣电影并进行简单可视化

先运行get_text.py会生成三个txt，后运行deal.py会生成数据处理后的图
文件说明：
msyh.ttc：字体，防止中文乱码
get_text.py  获取网页代码并处理格式，最后把数据写入txt
reviews_data.txt： 短评内容
reviews_date.txt： 短评日期
score.txt： 评分及相应的比例
deal.py：对上一步产生的数据进行可视化
四张图

import requests
from lxml import etree
import os,re,json,time,csv


#定义常量
url_detail = "https://www.amazon.com/dp/B000KBEA28"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
headers = {'User-Agent':user_agent}
#300个请求以内不用动态user—agent
# def randHeader():
#  	head_connection = ['Keep-Alive', 'close']
# 	head_accept = ['text/html, application/xhtml+xml, */*']
# 	head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
#  	head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
# 	 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
# 	'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
# 	'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
# 	'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
# 	'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
# 	'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
# 	'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
# 	'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
# 	'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
# 	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
# 	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
# 	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
# 	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
# 	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
# 	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
# 	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
# 	'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
# 	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
# 	header = {
# 	'Connection': head_connection[0],
# 	'Accept': head_accept[0],
# 	'Accept-Language': head_accept_language[1],
# 	'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
# 	}
# 	return header

def get_html_text(url):
	try:
		html = requests.get(url,headers = headers)
		html.ecoding = "utf-8"
		return html.content
	except:
		print("html read err")
		return ""

def trim_nowrap(str):
	return " ".join(str.split())

def trim_to_product(tem):
	for t in tem:
		str = t.xpath('string(.)')
	return str


def parse_page(templist,html):
	try:
		selector = etree.HTML(html)
		templist["title"] = trim_nowrap(selector.xpath('//*[@id="productTitle"]/text()')[0])
		templist["price"] = selector.xpath('//*[@id="priceblock_ourprice"]/text()')[0]

		featureinfo = []
		for each in selector.xpath('//*[@id="feature-bullets"]/ul/li/span/text()'):
			featureinfo.append(trim_nowrap(each))
		templist["feature"] = featureinfo[2:]
		#单独抓取的数据
		# templist["brand"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[1]/td')))
		# templist["model"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[2]/td')))
		# templist["item_weight"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[3]/td')))
		# templist["package_dimensions"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[4]/td')))
		# templist["alifornia"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[5]/td')))
		# templist["model_number"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[6]/td')))
		# templist["manufacturer_part_number"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[7]/td')))
		# templist["oem_part_number"] = trim_nowrap(trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]/tr[8]/td')))
		templist["detail"]  = trim_to_product(selector.xpath('//*[@id="productDetails_techSpec_section_1"]')).replace(' ',"").replace('\r',"").replace('\n'," ")
		#获得图片相关url
		script = selector.xpath('//*[@id="imageBlock_feature_div"]/script/text()')[0]
		script_str = script.replace(" ","").replace("\t","").replace("\n","").strip()
		image_script= re.findall('initial\':(.*?)\},\'colorToAsi', script_str)[0]
		image_html = json.loads(image_script)
		templist["image"] =[]
		for each in image_html:
			templist["image"].append(each["large"])
		return templist
	except:
		print("parse err")
		return ""


data_list = []
#打开目录下的resource文件，里面放亚马逊的关键数据
with open("resource.txt", 'r+')as f:
	lines =f.readlines()
	for line in lines:
		data_list.append(line.replace('\n',""))

file = os.getcwd() + '/amazon.csv'
with open(file,"a+") as datacsv:
	csvwriter = csv.writer(datacsv,dialect=("excel"))
	csvwriter.writerow(["item","url","title","price","image_url","feature","detail"])
	for i in data_list:
		infolist = {}
		url = "http://www.amazon.com/dp/"+str(i)
		info = parse_page(infolist,get_html_text(url))
		print(info)
		csvwriter.writerow([i,url,info["title"],info["price"],info["image"],info["feature"],info["detail"]])
		time.sleep(3)
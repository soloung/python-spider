import requests 
import re
import os

    
headers = {
    'Host': 'blog.csdn.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

url = 'http://tieba.baidu.com/p/5086069326' 
r = requests.get(url) 
print requests.utils.get_encodings_from_content(r.text)

testStr=r.content

eg = r'src="(.+?\.jpg|.+?\.png)'
imgre = re.compile(eg)
listurl = imgre.findall(testStr)
a = 0;
path = "F:\\funnyCode\\image\\"
for url in listurl:
    print url
    print '  '
    try:
        imageContent = requests.get(url)


        imageName = str(a) + '.jpg'
        a = a+1
        dest_dir=os.path.join(path,imageName)
        with open(dest_dir, "wb") as code:
            code.write(imageContent.content)
    except Exception , e:
        pass;
    finally:
        pass


# 
# dest_dir=os.path.join(path,"aaa.png")  
# print dest_dir



#eg = r'src="(.+?\.jpg)"'
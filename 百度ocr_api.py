# -*- coding: UTF-8 -*-  

from aip import AipOcr


# 定义常量  
APP_ID = '10764564'
API_KEY = 'TxvXG9liAGvVVpSuYGZ0iwXW'
SECRET_KEY = 'QG8SWcX4l98Q5HGxRhAnBKqhK9VmYGZL'

# 初始化文字识别分类器
aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片  
filePath = "wenzi.png"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 网络图片文字文字识别接口
result = aipOcr.webImage(get_file_content(filePath),options)

# 如果图片是url 调用示例如下
# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')

print(result)

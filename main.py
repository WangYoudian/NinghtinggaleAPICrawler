"""
1. 请求API主页的URL获取HTML内容
2. 从HTML中解析出5类重要接口二级页面地址
3. 请求二级页面内容并逐次解析出 接口功能 请求code和URL 请求参数 （返回参数），构造json内存对象（同时要将请求参数也保存成json格式而不是字符串）
4. 保存成json文件

例如：
{
    "监控数据": [
        {
            "上报数据": {
                "code": "POST http://127.0.0.1:2058/api/collector/push, POST /api/transfer/push",
                "请求样例": "a string which stands for an object",
                "返回样例": "optional, also a string which stands for an object"
            }
        },
        {
            "查询tags": {

            }
        }
    ],
}

"""



import requests
from bs4 import BeautifulSoup


URL = 'https://n9e.didiyun.com/docs/api/'

html = requests.get(url=URL).content
print(html)

bs = BeautifulSoup(html, 'html.parser')
print(bs.prettify())

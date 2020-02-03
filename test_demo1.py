import pytest
import requests

# 方法的命令必须以test_下划线开头
def test_request_login():  
    url = "http://192.144.148.91:2333/login"
    header = {"Content-Type":"application/json"}
    data = {"username":"applee","password":"12345678"}

    # 1.构造请求
    res = requests.post(url=url,headers=header,json=data)
   
    # 2.判断http状态码 
    assert res.status_code == 200  #判断http服务器响应状态码的值，判断的是服务器可不可用
    assert res.json()["status"] == 200  #判断取返回值里面的status，判断的是接口的功能


def test_zhuce():
    pass
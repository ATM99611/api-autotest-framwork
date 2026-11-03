import requests
import jsonpath

from config.url import base_url2
c1 ={"method":"post", # 变量接受,数据,"请求参数"
       "url":base_url2, # 服务器地址
       "params":None, # 请求参数
       "headers":None,      # 请求头
       "json":{"email": "eve.holt@reqres.in", "password": "cityscapes"}, # 请求体的json格式
       'data':None,  # 请求体的键对值传参
       'files':None, # 用于文件上传
}
mo =requests.request(**c1)
print(jsonpath.jsonpath(mo.json(),"$..token")[0])

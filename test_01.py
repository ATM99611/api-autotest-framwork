
from jinja2 import Template
import jsonpath
import pymysql
import pytest
import requests
from utils.QQ import mo3
from utils.ALLURE import mo1, mo2, mo4, mo5
from utils.excel_utils import execl
from config.url import base_url2


# class Test01: # 定义一个测试类
#     """获取cookies"""
#     def test_01(self): #定义一个测试函数/方法
#         s1 ={"method":"get","url": "https://httpbin.org/get"} # 封装请求方式为查询
#         s2 ={"method":"get","url": "https://httpbin.org/post",  # 封装请求方式为登录,并带上条件
#              "json":{"username":"admin","password":"123456"}}  #带上json条件
#         s =requests.Session() #自动获取cookies设置
#         so1 =s.request(**s1) # 获取so1的cookies
#         so2 =s.request(**s2) # 获取so2的cookies
#         print(so2.text.encode("utf-8"),decode("unicode_escape")) # 重新编码进行转换为显示中文
#         print(so1.text.encode("utf-8"),decode("unicode_escape")) # 重新编码进行转换为显示中文
#
#
#     """获取token"""
#     # 定义一个方法
#     def test_02(self):
#         # 变量接收一个请求方式为登录带url和json格式请求体的数据
#         m1 =requests.post("https://httpbin.org/post",
#                           json={"username":"admin","password":"123456"})
#         # 自动获取token,后面使用json表达式
#         token = jsonpath.jsonpath(m1.json(), "$..token")
#         # 封装进请求头中
#         headers = {"Authorization": f"Bearer {token}"}
#         # 发起登录请求,带上token值
#         m2 =requests.post("https://httpbin.org/post", headers=headers)
#         print(m2.text.encode("utf-8"),decode("unicode_escape"))

class Test02: #
    m1 =execl()
    all ={}
    @pytest.mark.parametrize("mo",m1)
    def test_01(self,mo):
        all =self.all
        mo =eval(Template(str(mo)).render(all))

        mo1(mo)


        request_data =mo2(mo)

        resp = mo3(**request_data)

        # print("数据",jsonpath.jsonpath(resp.json(),"$..token")[0])

        print("数据",resp.text)
        print("文件名",jsonpath.jsonpath(resp.json(),"$..files"))

        mo4(mo,resp)


        if mo["sql_check"] and mo["sql_expected"]:

            assert mo5(mo["sql_check"]) == mo["sql_expected"]
        #
        if mo["jsonExData"]:
            for keys,values in eval(mo["jsonExData"]).items():
               values=jsonpath.jsonpath(resp.json(),values)[0]
               all[keys]=values
        #
        if mo["sqlExData"]:
            for keys,values in eval(mo["sqlExData"]).items():
                values=mo5(values)
                all[keys]=values


















import allure
import jsonpath
import pymysql
import requests

from config.url import base_url2

@allure.story("all封装")
def mo1(mo):
        allure.dynamic.feature(mo["feature"])
        allure.dynamic.story(mo["story"])
        allure.dynamic.title(f"{mo["id"]}-----{mo["title"]}")

@ allure.suite("excel赋值")
def mo2(mo):
        method = mo["method"]
        url = base_url2 + mo["path"]
        headers = eval(mo["headers"]) if isinstance(mo["headers"], str) else None
        params = eval(mo["params"]) if isinstance(mo["params"], str) else None
        data = eval(mo["data"]) if isinstance(mo["data"], str) else None
        json = eval(mo["json"]) if isinstance(mo["json"], str) else None
        files = eval(mo["files"]) if isinstance(mo["files"], str) else None

        request_data = {"method": method,
                        "url": url,
                        "headers": headers,
                        "params": params,
                        "data": data,
                        "json": json,
                        "files": files
                        }
        return request_data

def mo3(**request_data):
    resp =requests.request(**request_data)
    return resp

def mo4(mo,resp):
    if mo["check"]:
        assert jsonpath.jsonpath(resp.json(), mo["check"])[0] == mo["expected"]
    else:
        assert mo["expected"] in resp.text

def mo5(sql,index=0):
    conn = pymysql.Connection(
        host="localhost",
        user="root",
        password="Qq5201314",
        database="mo",
        charset="utf8mb4")
    cur = conn.cursor()
    cur.execute(sql)
    m1 = cur.fetchone()
    cur.close()
    conn.close()
    return m1[index]




import requests
conn ={
    "method":"POST",
    "url":"http://127.0.0.1:8888/api/private/v1/load",
    "data":{"username":"admin","password":"123456"},
}
mo ={
    "method":"POST",
    "url":"http://httpbin.org/post",
    "headers":None,
    "files":None,
}


# token=conn.json()["token"]
# mo["headers"]={"AuthorList":token}
m1 =open("./file/123.png","rb")
mo["files"]={"file":("123.png",m1,"png")}
resp =requests.request(**mo)
print(resp.text)
print(resp.status_code)

{"file":("123.png",open("./file/123.png","rb"),"png")}
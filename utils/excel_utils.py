import openpyxl
from config.url import base_url1
# 第二胡个测试类,用于Excel文档读取
# 定义一个空字典用于后面的封装

# 导入包使用openpyxl,使用load打开文件
workbook = openpyxl.load_workbook("C:/Users/ASUS/PycharmProjects/过手/data/工作表.xlsx")
# 指定文件力的表存入变量中
worksheet = workbook["Sheet1"]
def execl():    # 定义一个测试函数/方法
    data = []
    # 使用for循环提取表中的数据.从第二行开始
    keys =[x.value for x in worksheet[2]] # 使用列表生成式不断循环加入键值对格式里面作为键部分
    for x in worksheet.iter_rows(min_row=3,values_only=True ):
        dict_dic =dict(zip(keys,x)) # 使用zip打包成元组,再用强行转换为字典
        if dict_dic["is_true"]:
            data.append(dict_dic) # 循环打印进空字典
    workbook.close() # 关闭文件

    return data # 返回数据
execl()


import pytest
import os

if __name__ == '__main__':
    pytest.main(["-vs","C:/Users/ASUS/PycharmProjects/过手/test_01.py","--alluredir","./report/json_report","--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")





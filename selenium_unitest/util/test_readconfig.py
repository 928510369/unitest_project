import configparser
cf=configparser.ConfigParser()
cf.read(r"E:\python\projects\pythonpractice\selenium_project\selenium3py3_tests\config\LocalElements.ini")
print(cf.get("RegisterElement","user_email"))
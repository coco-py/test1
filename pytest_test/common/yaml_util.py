import os

import yaml




class YamlUtil:


    #读取extract.yaml文件
    def read_extract_yaml(self,key):
        with open(os.getcwd()+"/extract.yml",mode="r",encoding="utf-8") as f:
            value=yaml.load(f,yaml.FullLoader)
            return value[key]



    #写入extract.yaml文件
    def write_extract_yaml(self,data):          #这边参数位置一定要写data，踩坑了！！！
        with open(os.getcwd()+"/extract.yml",mode="a",encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)


    #清除extract.yml文件
    def cleam_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml",mode="w",encoding="utf-8") as f:
            f.truncate()


    #读取extract.yaml文件
    def read_testcase_yaml(self,yaml_name):
        with open(os.getcwd()+"/testcase/"+yaml_name,mode="r",encoding="utf-8") as f:
            value=yaml.load(f,yaml.FullLoader)
            return value
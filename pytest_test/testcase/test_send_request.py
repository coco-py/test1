import re
import time

import pytest
import requests
from  common.yaml_util  import  YamlUtil






class TestSendRequest:


    # def setup(self):
    #     print("在每个用例之前执行")
    #
    # def teardown(self):
    #     print("在每个用例之后执行一次")


    #类变量：通过类名访问
    # access_token=""
    # csrf_token=""
    session=requests.session()

    ##需要带请求头的接口以及需要cookie关联的接口如何测试
    @pytest.mark.parametrize("caseinfo",YamlUtil().read_testcase_yaml("get_token.yaml"))   #读取测试用例的yaml
    # @pytest.mark.run(order=1)
    # @pytest.mark.smoke
    def test_start(self,caseinfo):
        print(caseinfo["name"])
        #发送get请求
        url=caseinfo["request"]["url"]
        method=caseinfo["request"]["method"]
        rep=TestSendRequest.session.request(method,url=url)
        #通过正则表达式获取鉴权码
        YamlUtil().write_extract_yaml({"csrf_token":re.search('name="csrf_token" value="(.*?)"',rep.text)[1]})          #使用封装方法来进行获取tonken

    #
    #
    # #需要带请求头的接口

    # @pytest.mark.run(order=2)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo",YamlUtil().read_testcase_yaml("post_elit.yaml"))
    def test_login(self,caseinfo):
        print(caseinfo["name"])

        csrf_token=YamlUtil().read_extract_yaml("csrf_token")
        #使用封装方法来进行获取tonken
        method=caseinfo["request"]["method"]
        url=caseinfo["request"]["url"]
        data=caseinfo["request"]["data"]
        headers=caseinfo["request"]["headers"]
        # time.sleep(4)
        rep=TestSendRequest.session.request(method,url,data=data,headers=headers)
        print(rep.json())
        # assert 'state' in 'success'

if __name__=="__main__":
    pytest.main(["-vs","./test_send_request.py"])
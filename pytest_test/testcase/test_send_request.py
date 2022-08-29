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

    #需要带请求头的接口以及需要cookie关联的接口如何测试
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_start(self):
        #发送get请求
        url="http://47.107.116.139/phpwind/"
        rep=TestSendRequest.session.request("get",url=url)
        #通过正则表达式获取鉴权码
        YamlUtil().write_extract_yaml({"csrf_token":re.search('name="csrf_token" value="(.*?)"',rep.text)[1]})        #使用封装方法来进行获取tonken
        # TestSendRequest.csrf_token=re.search('name="csrf_token" value="(.*?)"',rep.text)[1]
        # print(TestSendRequest.csrf_token)
        # assert "url" in rep.json()


    #需要带请求头的接口
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_login(self,conn_database):
        csrf_token=YamlUtil().read_extract_yaml("csrf_token")                                                          #使用封装方法来进行获取tonken
        url="http://47.107.116.139//phpwind/index.php?m=u&c=login&a=dorun"
        data={
            "username":"cgf",
            "password":"123456",
            "csrf_token":csrf_token,
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers={
            "Accept":"application/json, text/javascript, /; q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        # time.sleep(4)
        rep=TestSendRequest.session.request("post",url,data=data,headers=headers)
        print(rep.json())
        assert 'state' in 'success'

if __name__=="__main__":
    pytest.main(["-vs","./test_send_request.py"])
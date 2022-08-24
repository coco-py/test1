import re
import time

import pytest
import requests



class TestSendRequest:

    # def setup(self):
    #     print("在每个用例之前执行")
    #
    # def teardown(self):
    #     print("在每个用例之后执行一次")


    #类变量：通过类名访问
    access_token=""
    csrf_token=""
    # cks =""
    session=requests.session()



    #需要带请求头的接口以及需要cookie关联的接口如何测试
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_start(self,conn_database):
        #发送get请求
        url="http://47.107.116.139/phpwind/"
        rep=TestSendRequest.session.request("get",url=url)
        # print(rep.text)
        # TestSendRequest.access_tonken=req.json()["access_token"]
        #通过正则表达式获取鉴权码
        TestSendRequest.csrf_token=re.search('name="csrf_token" value="(.*?)"',rep.text)[1]
        print(TestSendRequest.csrf_token)
        # TestSendRequest.cks= rep.cookies
        # print(TestSendRequest.cks)


    #需要带请求头的接口
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_login(self):

        url="http://47.107.116.139//phpwind/index.php?m=u&c=login&a=dorun"
        data={
            "username":"cgf",
            "password":"123456",
            "csrf_token":TestSendRequest.csrf_token,
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



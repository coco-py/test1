import pytest

class TestApi:

    #基础用法
    @pytest.mark.parametrize("args",["扣扣","cgf","big"])
    def test_api(self,args):
        print(args)

    #解包
    @pytest.mark.parametrize("name,age",[["扣扣",10],["cgf",18]])
    def test_api2(self,name,age):
        print(name,age)



if __name__=="__main__":
    pytest.main(["-vs","test_api.py"])
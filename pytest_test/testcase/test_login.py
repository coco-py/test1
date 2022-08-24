import time

import pytest


class TestLogin:
    age=17

    @pytest.mark.usermanage
    def test_01_coco(self):
        print("测试cgf")

    @pytest.mark.usermanage
    @pytest.mark.skipif(age>=18,reason="已成年")
    def test_02_kele(self):
        print("打印可乐")

    @pytest.mark.run(order=1)
    @pytest.mark.usermanage
    @pytest.mark.skip(reason="雪碧太难喝")
    def test_03_xuebi(self):
        print("打印雪碧")

    @pytest.mark.run(order=2)
    @pytest.mark.usermanage
    def test_04_kuer(self):
        print("打印酷儿")
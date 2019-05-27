import allure


class TestPng:
    def test_png(self):
        with open("C:\\Users\\Administrator\\Desktop\\app08\\scripts\\adb.png", "rb") as f:
            allure.attach("图片", f.read(), allure.attach_type.PNG)

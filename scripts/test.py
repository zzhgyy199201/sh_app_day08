import allure,pytest


class Test001:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是测试一步骤")
    def test_001(self):
        print("-->test_001")
        allure.attach("标题001", "001具体的描述内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是测试二步骤")
    def test_002(self):
        allure.attach("标题002", "002具体的描述内容")
        print("-->test_002")
        assert False

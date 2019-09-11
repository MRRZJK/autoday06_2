
import pytest


class TestLogin:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test001(self):
        print("test001被执行")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test002(self):
        print("test002被执行")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test003(self):
        print("test003被执行")

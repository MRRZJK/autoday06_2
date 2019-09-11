import allure


class TestLogin:
    @allure.step(title="我是执行第一步")
    def test001(self):
        allure.attach("心情不好","因为我饿了")
        print("test001被执行")

    @allure.step(title="我是执行第二步")
    def test002(self):
        allure.attach("哎", "因为我饿了")
        print("test002被执行")
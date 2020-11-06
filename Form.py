import http3
class Form():
    url = ''
    def __init__(self, login='admin', password='admin', age=21, url=''):
        self.user_name = login
        self.user_password = password
        self.user_age = age
        self.url = url
        print("Ваш логин {} и пароль {}, Вам {} лет, ссылка на ваш сайт {}".format(self.user_name,
                                                                                   self.user_password,
                                                                                   self.user_age,
                                                                                   self.url))
    def s_code(self, url):
        self.h_code = http3.get(url)
        self.status_code = self.h_code.status_code
        return self.status_code


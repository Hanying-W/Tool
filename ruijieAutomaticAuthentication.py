# !/bin/python3
# -*-coding:utf-8-*-
import requests
import sys
import urllib

user = "输入你的账号"
pwd = "输入你的密码"
service = "选择连接方式"

if user == '在此输入用户名' or pwd == '在此输入密码' or service == '在此输入运营商（移动、电信等）':
    if len(sys.argv) != 4:
        print("Usage:\npython ruijie_python.py username password service")
        exit(0)
    else:
        user = sys.argv[1]
        pwd = sys.argv[2]
        service = sys.argv[3]


def login(re, user, pwd, service):
    Referer = re.text.split("'")[1]
    URL = Referer.split("?")[0].replace('index.jsp', 'InterFace.do')
    queryString = Referer.split("?")[1]
    queryString = queryString.replace('&', "%2526")
    queryString = queryString.replace('=', "%253D")
    service = urllib.parse.quote(urllib.parse.quote(service))
    headers = {
        "Accept": "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cookies": "EPORTAL_COOKIE_USERNAME=; EPORTAL_COOKIE_PASSWORD=; EPORTAL_COOKIE_SERVER=; "
                   "EPORTAL_COOKIE_SERVER_NAME=; EPORTAL_AUTO_LAND=; EPORTAL_USER_GROUP=; "
                   "EPORTAL_COOKIE_OPERATORPWD=;",
        "Content-Type": "application/x-www-form-urlencoded",
        "referer": Referer,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 "
                      "Safari/537.36 "
    }
    login_info = "userId={}&password={}&service={}&queryString={" \
                 "}&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false".format(
        user, pwd, service, queryString)
    logging = requests.session().post(URL, data=login_info, headers=headers, params={"method": "login"})
    print(logging.content.decode('utf-8'))


def main():
    re = requests.get("http://www.google.cn/generate_204")
    if re.status_code == 204:
        print("You Are Already Online!")
    else:
        login(re, user, pwd, service)


if __name__ == '__main__':
    main()

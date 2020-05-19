import requests
import multiprocessing

URL = 'https://www.biquge.com.cn/book/'


# 检查小说属于哪个范畴
# 0代表不存在
# 1代表正在连载
# 2代表已完结
def getHtml(url):
    html = requests.get(url)
    s = html.text
    if 'listindex' in s:
        if '连载中' in s:
            return 1
        return 2
    return 0


def Transit(i, j):
    for k in range(i, j):
        sign = getHtml(URL + str(k) + '/')
        if sign == 0:
            print("未找到标号为{}的小说".format(k))
        elif sign == 1:
            file = open('SerializeName.txt', 'a')
            file.write(str(k) + '\n')
            file.close()
            print("编号为{}的小说正在连载".format(k))
        elif sign == 2:
            file = open('EndName.txt', 'a')
            file.write(str(k) + '\n')
            file.close()
            print("编号为{}的小说正在连载中".format(k))


if __name__ == '__main__':
    # 格式说明
    # 变量名 = 函数名(target={要执行的函数名} , args={[参数][,][参数][,][参数][,][参数][,]})
    # 如果有参数，则最后一位一定是要逗号
    # 没有参数则可以省略
    process0 = multiprocessing.Process(target=Transit, args=(7500, 7885,))
    # 格式说明
    # 变量名.start()
    # 开始执行
    process0.start()
    # 格式说明
    # 变量名.join()
    # 阻塞进程，把当前进程执行完毕后再执行下面进程
    process0.join()

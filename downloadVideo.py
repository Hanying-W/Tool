import sys
import you_get
import os

name = os.getcwd() + '/Video'

url = input("请输入下载网址：")

sys.argv = ['you-get', '-o', name, url]

you_get.main()

if __name__ == '__main__':
    file = open('SpawnMultipleProcesses.txt', 'w')
    FunctionName = input("请输入函数名：")
    Count = int(input("请输入要创建的进程数："))
    sign = input("是否有变量(Y/N)：")
    if sign in ['Y', 'y']:
        for i in range(Count):
            name = 'process' + str(i) + ' = Process(target=' + FunctionName + ', args=('
            Variable = input("请输入变量并以空格隔开：").split()
            for j in Variable:
                name = name + j + ','
            name = name + '))'
            file.write(name + '\n')
            print("插入成功")
    else:
        for i in range(Count):
            name = 'process' + str(i) + ' = Process(target=' + FunctionName + ', args=())'
            file.write(name + '\n')
            print("插入成功")
    for i in range(Count):
        t = 'process' + str(i) + '.start()'
        file.write(t + '\n')

    for i in range(Count):
        t = 'process' + str(i) + '.join()'
        file.write(t + '\n')

    file.close()


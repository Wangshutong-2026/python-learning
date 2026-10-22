try:
    with open('tasks.txt', 'r') as f:
        contend = f.read()
        if contend == '':
            tasks = []
        else:
            tasks = contend.split('\n')  #太严谨了
except FileNotFoundError:
    tasks = []

# tasks = []   #列表用复数，养成好习惯
while True:
    word = input("请输入您的选择")
    if word =='添加任务' or word == '1':
        try:
            num = int(input("请输入您要添加的任务数量"))
            for i in range(num):    #range()是函数，不要忘记()
                #循环变量一般用_和i表示，表示“我只想循环几次，不在乎这个数字”
                task_name = input("请输入您的任务名")
                tasks.append(task_name)
            with open('tasks.txt', 'w') as f:    #w+可读可写，但是也是重新编辑，a才是追加，不清空
                f.write('\n'.join(tasks))
            print('保存成功！')
        except ValueError:
            print('输入信息错误，任务数量必须是纯数字，请重新选择！')
        # print(tasks)
    if word =='查看任务' or word == '2':
        # for n in tasks:
        #     print(n)
        with open('tasks.txt', 'r') as f:
            print(f.read())
    if word =='删除任务' or word == '3':
        try:
            text = input('请输入你要删除的任务名')
            tasks.remove(text)
            with open('tasks.txt', 'w') as f:
                f.write('\n'.join(tasks))
            print('删除成功！')
        except ValueError:
            print('未查找到相应任务名，请重新输入')
    if word =='退出' or word == '4':
        break



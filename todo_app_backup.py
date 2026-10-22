try:
    with open('tasks.txt', 'r') as f:
        content = f.read()
        if content == '':
            tasks = []
        else:
            tasks = content.split('\n')  #太严谨了
except FileNotFoundError:
    tasks = []
def add_task(tasks):     #要有参数！！！
    try:
        num = int(input("请输入您要添加的任务数量"))
        for i in range(num):  # range()是函数，不要忘记()
            # 循环变量一般用_和i表示，表示“我只想循环几次，不在乎这个数字”
            task_name = input("请输入您的任务名")
            tasks.append(task_name)
        with open('tasks.txt', 'w') as f:  # w+可读可写，但是也是重新编辑，a才是追加，不清空
            f.write('\n'.join(tasks))
        print('保存成功！')
    except ValueError:
        print('输入信息错误，任务数量必须是纯数字，请重新选择！')
def show_tasks(tasks):
    for n in tasks:
         print(n)
def del_task(tasks):
    try:
        text = input('请输入你要删除的任务名')
        tasks.remove(text)
        with open('tasks.txt', 'w') as f:
            f.write('\n'.join(tasks))
        print('删除成功！')
    except ValueError:
        print('未查找到相应任务名，请重新输入')
while True:
    word = input("请输入您的选择")
    if word == '添加任务' or word == '1':
        add_task(tasks)
    elif word =='查看任务' or word == '2':
        show_tasks(tasks)
    elif word == '删除任务' or word == '3':
        del_task(tasks)
    elif word == '退出' or word == '4':
        print('退出完成！')
        break
    else:
        print("输入错误，请重新输入")

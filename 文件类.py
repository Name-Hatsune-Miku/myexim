# 请封装设计一个操作文件和文件夹类，能够更加方便的使用?
import os

class File:
    def __init__(self, name):
        self.name = name

    def create(self):
        with open(self.name, 'w') as file:
            pass
        print(f'{self.name} 已创建')

    def delete(self):
        os.remove(self.name)
        print(f'{self.name} 已删除')


# 创建
filecreate = input('是否选择文件创建(填是或不是): \n')
if filecreate == '是':
    name = input("请输入文件名(带后缀): \n")
    file = File(name)
    file.create()
else:
    print('不创建')
# 删除
filedelete = input('是否选择文件删除(填是或不是): \n')
if filedelete == '是':
    name = input("请输入文件名(带后缀): \n")
    file = File(name)
    file.delete()
else:
    print('不删除')
# 文件备份
bak = input('是否选择文件备份(填是或不是): \n')
if bak == '是':
    old_name = input("请输入备份文件名: \n")


    def backup(old_name):
        index = old_name.rfind('.')
        new_name = old_name[:index] + '_bak' + old_name[index:]
        old_file = open(old_name, 'rb')
        new_file = open(new_name, 'wb')
        while True:
            data = old_file.read(1024)
            if len(data) == 0:
                break
            new_file.write(data)
        old_file.close()
        new_file.close()


    backup(old_name)
    print('备份成功')
else:
    print('不备份')

print('hello world')
# print(value, ..., sep=' ', end='ln')
# 1.这里的value如果输入一个或多个，则打印一个或多个
# 2.sep 代表可自定义value之间的符号，默认为空值
# 3.end代表可自定义value结尾的符号，默认为换行符号
'''
多行注释
'''
print('hello', 'world')
print('hello', 'world', sep=',')
print('hello', 'world', \
      sep=',', end='.')

# python是以缩进来包含的，而不是大括号
# 格式化快捷键设置为：ctrl+l
for i in range(10):
    print(i)

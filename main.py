# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""他写了我就写点啥"""
__authon__ = 'hstking hst_king@hotmail.com'


def strCase():
    "字符串大小写转换"
    print("演示字符串大小写转换")
    print("字符串S赋值为：‘ThIs is a PYTHON'")
    S = 'ThIs is a PYTHON'
    print("大转小：\tS.lower() \t= %s" % (S.lower()))
    print("小转大：\tS.upper() \t= %s" % (S.upper()))
    print("大小转换：\t\tS.swapcase() \t= %s" % (S.swapcase()))
    print("首字母大写： \t\tS.title() \t=%s" % (S.title()))
    print('\n')


def strFind():
    """字符串搜索，替换"""
    print("演示字符串搜索，替换等")
    print("字符串S赋值为：‘ThIs is a PYTHON'")
    S = ' ThIs is a PYTHON '
    print("字符串搜索：\t\tS.find('is') \t= %s" % (S.find('is')))
    print("字符串统计：\t\tS.count('s') \t= %s" % (S.count('s')))
    print("字符串替换： \t\tS.replace('IS','is') = %s" % (S.replace('IS', 'is')))
    print("去左右空格：\t\tS.strip() \t=#%s#" % (S.strip()))
    print("去左空：\t\tS.lstrip() \t=#%s#" % (S.lstrip()))
    print("去右空：\t\tS.rstrip() \t=#%s#" % (S.rstrip()))
    print('\n')


def strSplit():
    print("字符串分割，组合")
    print("字符串S赋值为：‘ThIs is a PYTHON'")
    S = ' ThIs is a PYTHON '
    print("分割s： \t\tS.split() \t = %s" % (S.split()))
    print("组合s 1:'#'.join(['this','is','a','python']) \t= %s" % '#'.join(['this', 'is', 'a', 'python']))
    print("组合s 2:'$'.join(['this','is','a','python']) \t= %s" % '$'.join(['this', 'is', 'a', 'python']))
    print("组合s 3:' '.join(['this','is','a','python']) \t= %s" % ' '.join(['this', 'is', 'a', 'python']))
    print('\n')


def strTest():
    """字符串测试"""
    print("演示字符串测试")
    print("演示字符串S赋值为：‘abcd’")
    S = 'abcd'
    print("测试S.isalpha() = %s" % (S.isalpha()))
    print("测试S.isdigit() = %s" % (S.isdigit()))
    print("测试S.isspace() = %s" % (S.isspace()))
    print("测试S.islower() = %s" % (S.islower()))
    print("测试S.isupper() = %s" % (S.isupper()))
    print("测试S.istitle() = %s" % (S.istitle()))
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strCase()
    strFind()
    strSplit()
    strTest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

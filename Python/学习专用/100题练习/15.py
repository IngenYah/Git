#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
grade = int(input('输入成绩:'))
if grade >= 90 and grade <= 100:
    print('A')
elif grade >= 60 and grade < 90:
    print('B')
elif grade >= 0 and grade < 60:
    print('C')
else:print('ERROR')
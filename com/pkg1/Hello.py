# coding=utf-8


# 集合 {}
student_set = {'张三', '李四', '王五'}

for item in student_set:
    print(item)

print('-----------')
for i, item in enumerate(student_set):
    print('{0} - {1}'.format(i, item))

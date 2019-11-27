# coding=utf-8


# 字典 {key1:value1, key2:value2}
student_dic = {101: "wangyu", 102: "lisue", 103: "huanghaipo"}

print('---key---')
for student_id in student_dic.keys():
    print("学号：" + str(student_id))

print('---value---')
for student_name in student_dic.values():
    print("名字：" + str(student_name))

print('------')
for student_id, student_name in student_dic.items():
    print("学号：{0} - 名字：{1}".format(student_id, student_name))

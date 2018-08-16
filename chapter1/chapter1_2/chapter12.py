from chapter1.chapter1_1 import chapter11

# 链表
print(chapter11.sent1)

chapter11.lexical_diversity(chapter11.sent1)

ex1 = ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']
print(sorted(ex1))
print(len(set(ex1)))
print(ex1.count("the"))

# 链表的连接
sent = chapter11.sent1 + chapter11.sent4
print(sent)

# 链表的追加
chapter11.sent1.append("some")

# 索引
demo_word = chapter11.text4[173]
chapter11.text4.index('awaken')
print(demo_word)

# 切片
demo_word = chapter11.text5[16715:16735]
print(demo_word)

# 体会运行时错误
# sent[100]

sent[5:8]

# 变量 赋值 变量 = 表达式
my_sent = ['Bravely', 'bold', 'Sir', 'Robin',
           'forth', 'Camelot', '.']
print(my_sent)

# 字符串
name = 'Monty'
print(name[0])

# 前第四个
print(name[:4])

# 倒数两个
print(name[-2:])

# 字符串乘法 和 加法
name = name * 2
print(name)

name = name + "!"
print(name)

# 拼接
words = "".join(['Monty', 'Python'])
print(words)
words = "Monty python"
split_words = words.split()
print(split_words)

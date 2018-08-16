import nltk
from nltk.book import *

# 下载全部
# nltk.download()

# 下载某一章节
# nltk.download('gutenberg')

# 搜索文本 一致
text1.concordance("monstrous")

# 相似查询
text1.similar("monstrous")

# 查找两个以上词汇 用来识别2个关键词相似的词语
text2.common_contexts(["monstrous", "very"])

# 画出美国总统就职演说词汇分布图
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# 生成随机文本 已经被注释了 nltk2.0可用
# text3.generate()

# 获取文本从头到尾的长度
len(text3)

# 对text3组成一个set，并排序
sorted(set(text3))

# 词汇丰富程度
len(text3) / len(set(text3))

# 某个词出现的次数
text3.count("smote")


# 词汇丰富程度简单函数
def lexical_diversity(text):
    lexical = len(text) / len(set(text))
    print(lexical)
    return lexical


lexical_diversity(text3)


# 某个词出现的百分比
def percentage(count, total):
    percent = count / total * 100
    print(percent)
    return percent


percentage(text4.count('a'), len(text4))

# 课本练习
text5.count("lol")
percentage(text5.count("lol"), len(text5))

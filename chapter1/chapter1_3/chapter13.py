from nltk.book import *

# 单词总数
fre_dist = FreqDist(text1)
print(fre_dist)

# 所有的不同链表
vocabulary = fre_dist.keys()
vocab = list(vocabulary)
print("vocabulary1=", vocab)
# 后面的参数是 绘制累计频率分布图
fre_dist.plot(50, cumulative=True)

# 高频词
whale_num = fre_dist['whale']
print(whale_num)

# 只出现一遍的词
fre_dist.hapaxes()

# 细粒度的选择词
text1_set = set(text1)
long_words = [w for w in text1_set if len(w) > 15]
print(sorted(long_words))

fre_dist = FreqDist(text5)
# 查找text5中 长度大于7 且出现频率也大于7 的词 并排序
print(sorted([w for w in set(text5) if len(w) > 7 and fre_dist[w] > 7]))

# 搭配 特点 其中的词不能被类似的词置换 获取搭配 从双连词开始
bigrams(['more', 'is', 'said', 'than', 'done'])

# 找出出现频率比预期更频繁的双连词
text4.collocations()

# 其他东西
[len(w) for w in text1]

#
fre_dist.items()
fre_dist.max()
# 以频率递减顺序排序的样本链表
fre_dist.keys()
# 频率
fre_dist.freq(3)
# 样本总数
fre_dist.N()
# 绘制分布表
fre_dist.tabulate()


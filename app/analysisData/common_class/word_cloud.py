# -*- coding:utf-8 -*-
"""
created by goblinM 2019.5.12
词云生成（热点词，关键字词云）
"""
from collections import Counter

from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from app.web.db_utils.mongodb import MongoDBUtils
import matplotlib.pyplot as plt
import numpy as np
class Word:
    def __init__(self,collectionName):
        self.mongo = MongoDBUtils(collectionName)
        self.path = r"D:\Django\NegativeInternet\app\analysisData\common_class\images"
        self.font = r"D:\Django\NegativeInternet\app\analysisData\msyh.ttc"
        # self.font_set = FontProperties(fname=r"D:\Django\NegativeInternet\app\analysisData\msyh.ttc", size=12)
        self.alice_mask = np.array(Image.open(self.path+r'\e.jpg'))

    def keywordcloud(self):
        """
        生成词云的图片
        :return: 图片
        """
        curInfo = self.mongo.searchByDoc({"_id":{"$regex":"巴黎圣母院"}})
        print(curInfo.count())
        # stopwords = set(STOPWORDS)
        self.stopwords = ["游戏","手机","没有","时候","可能","快递","有点","东西","女人","不能","觉得","看到"]
        with open('chineseStopWords.txt','r',encoding='gbk') as r:
            for w in r.readlines():
                self.stopwords.append(w)
        self.stopwords = set(self.stopwords)
        self.keywords = ""
        for data in curInfo:
            self.keywords = self.keywords +" "+data.get("keywords")
        wc = WordCloud(
            background_color='white',
            width=1000,
            height=800,
            font_path=self.font,
            mask=self.alice_mask,
            stopwords=self.stopwords
        )
        wc.generate_from_text(self.keywords)
        plt.imshow(wc)
        plt.axis("off")
        plt.figure()
        plt.show()
        wc.to_file(self.path+r"\new.png")
        self.mongo.close()

    def wordcount(self):
        """
        词频统计
        :return:图片以及数据
        """
        keywords_list = self.keywords.split()
        for k in list(keywords_list):
            if k in self.stopwords:
                keywords_list.remove(k)
        self.top20 = dict(Counter(keywords_list).most_common(20))
        print(self.top20)
        label = list(self.top20.keys())
        y = list(self.top20.values())
        idx = np.arange(len(y))
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.barh(idx, y)
        plt.yticks(idx + 0.4, label)
        plt.xlabel(u'出现次数', fontsize=20, labelpad=5)
        plt.ylabel(u'关键词', fontsize=20, labelpad=5)
        # plt.title(u'涡流发生器对激波串振荡的控制', fontsize=25)
        plt.savefig(self.path+u'\wordcount')
        plt.show()

    def wordpie(self):
        """
        pie级坐标图
        :return: 图片
        """
        # 绘制pie char on polar axis
        N = len(self.top20)
        label = list(self.top20.keys())
        y = list(self.top20.values())
        theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
        radii = y
        width = np.pi / 6
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        ax = plt.subplot(111, projection='polar')
        bars = ax.bar(theta, radii, width=width, bottom=0.0)
        plt.xticks(theta + np.pi / 12, label)
        for r, bar in zip(radii, bars):
            bar.set_facecolor(plt.cm.viridis(r / 10))
            bar.set_alpha(0.5)
        plt.savefig(self.path+u'\wordpie')
        plt.show()


if __name__ == '__main__':
    obj = Word('zhihu_paris')
    obj.keywordcloud()
    obj.wordcount()
    obj.wordpie()

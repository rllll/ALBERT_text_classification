# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-03-04 17:33

import time
import pandas as pd
import numpy as np
from albert_zh.extract_feature import BertVector
from keras.models import load_model
load_model = load_model("visit_classify.h5")

# 预测语句
texts = ['在访问限制中，用户可以选择禁用iPhone的功能，包括Siri、iTunes购买功能、安装/删除应用等，甚至还可以让iPhone变成一台功能手机。以下是访问限制具体可以实现的一些功能',
         'IT之家4月23日消息 近日，谷歌在其官方论坛发布消息表示，他们为Android Auto添加了一项新功能：可以访问完整联系人列表。用户现在可以通过在Auto的电话拨号界面中打开左上角的菜单访问完整的联系人列表。值得注意的是，这一功能仅支持在车辆停止时使用。',
         '要通过telnet 访问路由器，需要先通过console 口对路由器进行基本配置，例如：IP地址、密码等。',
         'IT之家3月26日消息 近日反盗版的国际咨询公司MUSO发布了2017年的年度报告，其中的数据显示，去年盗版资源网站访问量达到了3000亿次，比前一年（2016年）提高了1.6%。美国是访问盗版站点次数最多的国家，共有279亿次访问；其后分别是俄罗斯、印度和巴西，中国位列第18。',
         '应葡萄牙议会邀请，全国人大常委会副委员长吉炳轩率团于12月14日至16日访问葡萄牙，会见副议长费利佩、社会党副总书记卡内罗。',
         '2月26日至3月2日，应香港特区政府“内地贵宾访港计划”邀请，省委常委、常务副省长陈向群赴港考察访问，重点围绕“香港所长、湖南所需”，与特区政府相关部门和机构深入交流，推动湖南与香港交流合作取得新进展。',
         '目前A站已经恢复了访问，可以直接登录，网页加载正常，视频已经可以正常播放。',
         '难民署特使安吉丽娜·朱莉6月8日结束了对哥伦比亚和委内瑞拉边境地区的难民营地为期两天的访问，她对哥伦比亚人民展现的人道主义和勇气表示赞扬。',
         '据《南德意志报》报道，德国总理默克尔计划明年1月就前往安卡拉，和土耳其总统埃尔多安进行会谈。',
         '自9月14日至18日，由越共中央政治局委员、中央书记处书记、中央经济部部长阮文平率领工作代表团对希腊进行工作访问。',
         'Win7电脑提示无线适配器或访问点有问题怎么办?很多用户在使用无线网连接上网时，发现无线网显示已连接，但旁边却出现了一个黄色感叹号，无法进行网络操作，通过诊断提示电脑无线适配器或访问点有问题，且处于未修复状态，这该怎么办呢?下面小编就和大家分享下Win7电脑提示无线适配器或访问点有问题的解决方法。',
         '2019年10月13日至14日，外交部副部长马朝旭访问智利，会见智利外长里韦拉，同智利总统外事顾问萨拉斯举行会谈，就智利举办亚太经合组织（APEC）第二十七次领导人非正式会议等深入交换意见。',
         '未开发所有安全组之前访问，FTP可以链接上，但是打开会很慢，需要1-2分钟才能链接上',
         'win7系统电脑的用户，在连接WIFI网络网上时，有时候会遇到突然上不了网，查看连接的WIFI出现“有限的访问权限”的文字提示。',
         '联合国秘书长潘基文８日访问了日本福岛县，与当地灾民交流并访问了一所高中。',
         '国务院总理温家宝当地时间23日下午乘专机抵达布宜诺斯艾利斯，开始对阿根廷进行正式访问。',
         '正在中国访问的巴巴多斯总理斯图尔特１５日在陕西西安参观访问。',
         '据外媒报道,当地时间10日,美国白宫发声明称,美国总统特朗普将于2月底访问印度,与印度总理莫迪进行战略对话。',
         '2月28日，唐山曹妃甸蓝色海洋科技有限公司董事长赵力军等一行5人到黄海水产研究所交流访问。黄海水产研究所副所长辛福言及相关部门负责人、专家等参加了会议。',
         '2018年7月2日，莫斯科孔子文化促进会会长姜彦彬，常务副会长陈国建，在中国著名留俄油画大师牟克教授的陪同下，访问了莫斯科国立苏里科夫美术学院，受到第一副校长伊戈尔·戈尔巴秋克先生接待。'
         '据外媒报道，当地时间26日晚，阿尔及利亚总统特本抵达沙特阿拉伯，进行为期三天的访问。两国领导人预计将就国家间合作和地区发展进行磋商。',
         '与标准Mozy一样，Stash文件夹为用户提供了对其备份文件的基于云的访问，但是它们还使他们可以随时，跨多个设备(包括所有计算机，智能手机和平板电脑)访问它们。换句话说，使用浏览器的任何人都可以同时查看文件(如果需要)。操作系统和设备品牌无关。',
         '研究表明，每个网页的平均预期寿命为44至100天。当用户通过浏览器访问已消失的网页时，就会看到「Page Not Found」的错误信息。对于这种情况，相信大多数人也只能不了了之。不过有责任心的组织——互联网档案馆为了提供更可靠的Web服务，它联手Brave浏览器专门针对此类网页提供了一键加载存档页面的功能。',
         '据外媒报道，土耳其总统府于当地时间2日表示，土耳其总统埃尔多安计划于5日对俄罗斯进行为期一天的访问。',
         '3日，根据三星电子的消息，李在镕副会长这天访问了位于韩国庆尚北道龟尾市的三星电子工厂。'] * 10

labels = []

bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=100)

init_time = time.time()

# 对上述句子进行预测
for text in texts:

    # 将句子转换成向量
    vec = bert_model.encode([text])["encodes"][0]
    x_train = np.array([vec])

    # 模型预测
    predicted = load_model.predict(x_train)
    y = np.argmax(predicted[0])
    label = 'Y' if y else 'N'
    labels.append(label)

cost_time = time.time() - init_time
print("Average cost time: %s." % (cost_time/len(texts)))

for text, label in zip(texts, labels):
    print('%s\t%s' % (label, text))

df = pd.DataFrame({'句子':texts, "是否属于出访类事件": labels})
df.to_excel('./result.xlsx', index=False)
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:26:29 2016

@author: @author: ifuturedata@icloud.com
Brief:
    1.邮件接卸得到标准字段：CVTable
    2.邮件解析路径
        1.赶集解析路径
        2.58解析路径
        3.智联解析路径
    3.简历文档解析路径
        1.赶集解析路径
        2.58解析路径
        3.智联解析路径
"""

class rgj_decode_td_xpath:

    # 简历基本信息
    id1_xpath= """//body/img/@src"""#应聘简历ID
    id2_xpath="""//*[@id='pageviews']/@data-puid"""#投递简历ID
    url2_xpath="""//tr[2]/td[7]/a/@href"""#投递简历获取简历URL
    CVDoc_xpath="""//*[@class='offercon pos-relat']"""#简历DIV部分
    CVtitle_xapth="""//*[@class='offer_tit']/text()"""#简历标题
    updateTime_xpath=""".//*[@class='offerxx']/p//span[1]/text()"""#简历更新时间
    # http://hrvip.ganji.com/disguise_static/mark_as_read.gif?uid=599847344&wid=2088113201&fid=2164042558&checksum=1f1f6bfec862350d43a09088477f1ef1\
    contact1_xpath= """//tr/td/div/span"""#应聘简历联系方式路径
    contact2_xpath="""//tr[2]/td[6]/text()"""
    city_xpath=""".//*[@class='crumbs clearfix']/a[1]/text()""" #招聘城市  上海58同城
    Industry_xpath=""".//"""#行业 上海人事/行政/后勤求职简历
    ara_xpath=""".//"""#区域 黄浦人事/行政/后勤求职简历


    # 基本信息
    CVName_xpath=""".//*[@class='offer_name']/text()"""#名字
    CV_Sex_Age_xpath=""".//*[@class='offer_age']/text()"""#性别-年龄
    EduBak1_xpath="""//ul[@class='offer_detail clearfix']/li[2]/span/text()"""#学历
    WorkExp_xpath="""//ul[@class='offer_detail clearfix']/li[4]/span/text()"""#工作经验 3-5年工作经验 工作经验需要去掉工作经验
    CurLoc_xpath="""//"""#现居地 现居岳阳君山区  去掉现居
    OriLoc_xpath="""//ul[@class='offer_detail clearfix']/li[6]/span/text()"""#籍贯

    # 基本补充
    isPhoneIden_xpath="""//*[@class='jpb-icon icon2']"""#是否手机认证
    postCnt_xpath="""//*[@id='deliverAndDownload']/em[1]/text()"""
    visitCnt_xpath="""//*[@id='pageviews']/em/text()"""
    downCnt_xpath="""//*[@id='deliverAndDownload']/em[2]/text()"""
    cvActive_xpath=""".//"""#用户是否活跃：可能找到工作标记
    cvActive_xpath2="""//"""#用户是否活跃：该简历已更新,点击查看

    # 求职意向
    # Exp_xpath="""//ul[@class='offer_detail clearfix']/li[1]"""#求职意向根路径
    ExpJob2_xpath="""//ul[@class='offer_detail clearfix']/li[1]/span/a/text()""" #期望职位2
    ExpLoc_xpath="""//ul[@class='offer_detail clearfix']/li[5]/span/text()""" #期望工作地 去掉 想在 xxx 工作
    Salary_xapth="""//ul[@class='offer_detail clearfix']/li[3]/span/text()""" #期望薪水 去掉 期望薪资 xxx

    # 自我介绍
    Introduction_xpath="""//*[@class='nrcon lht24']/p/text()"""#自我介绍
    Ability_xpath="""//*[@class='private-label clearfix']/span/text()""" #能力标签列表  列表拼接调用GetSelValue

    # 工作经验
    WorkExpDetail_xpath="""//*[@class='divide_tit']/span/text()"""#工作经验描述  具体工作时间需要解析 工作数需要解析 （工作了2年8个月，做了2份工作）
    WorkExp1_xpath="""//*[@class="nrcon workexp"][1]/p/text()"""#页面显示的第一个工作信息
    WorkExp2_xpath="""//*[@class="nrcon workexp"][last()]/p/text()"""#页面显示的最后一个工作信息

    # 教育经历/证书/专业技能
    Worktime_xpath="""//*[@class='nrcon worktime']"""
    Worktime_xpath2="""//*[@class='nrcon worktime']/p/text()"""

    # 语言能力
    Lang_xpath="""//*[@class='nrcon lht34']/p/text()"""#英语：一般

    # 培训
    Train_xpath="""//*[@class='nrcon train']/p[1]/text()"""

    # 作品
    ImageCnt_xpath="""//*[@class='gj-slide-thumbs']"""#照片数目  len(list)


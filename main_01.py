# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:26:29 2016

@author: @author: ifuturedata@icloud.com
Brief:
    1.职位描述分词
    2.职位画像表更新
       1) job_info_01(去重)
       2) job_info_02(分词)
       3)job_info_03(更新)
       4)job_info_04(更新)
       5)job_info_05(更新)
"""


from WordsDiv.WordsDiv import *

if __name__ == '__main__':
    Cost1 = Cost()
    test1 = MyWordsDiv()

    WebName = 'lagou'
    KeyWords2All = [
              '大数据', '大数据架构师', 'Java', 'Java系统架构师', 'HTML5', 'Web前端', '软件测试', 'UI设计',
              '.NET', 'C#', '数据分析', '数据挖掘', 'hadoop', 'IOS', 'PHP'
    ]
    KeyWords1 = ' '.join(KeyWords2All)
    # run_date=time.strftime("%Y-%m-%d",time.localtime())
    run_date = '2016-04-07'

    for KeyWords2 in KeyWords2All:
        # 1 job_info(去重)
        tmpTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print '=============================================================='
        print tmpTime+' 正在处理 关键字2='+KeyWords2+' ...'
        print tmpTime+'正在执行:1 job_info(去重)...'
        msg1 = test1.DuplicateCheck(WebName,KeyWords1,KeyWords2,run_date)
        print msg1
        # 2 job_info_02(分词)
        tmpTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print '=============================================================='
        print tmpTime+'正在执行:2 job_info_02(分词)...'
        msg2 = test1.LagouWordsDiv(WebName,KeyWords1,KeyWords2,run_date)
        # 3 job_info_03(更新)
        tmpTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print '=============================================================='
        print tmpTime+'正在执行:3 job_info_03(更新)...'
        msg3=test1.Update_job_info_03(WebName,KeyWords1,KeyWords2,run_date)
        # 4 job_info_04(更新)
        tmpTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print '=============================================================='
        print tmpTime+'正在执行:4 job_info_04(更新)...'
        msg4 = test1.Update_job_info_04(WebName,KeyWords1,KeyWords2,run_date)
        # 5 job_info_05(更新)
        tmpTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print '=============================================================='
        print tmpTime+'正在执行:5 job_info_05(更新)...'
        msg5 = test1.Update_job_info_05(WebName,KeyWords1,KeyWords2,run_date)
        print tmpTime+' 关键字2='+KeyWords2+' 已经处理完毕...'
        Cost1Sec = Cost1.Cost()
    test1.CloseDB()  #关闭数据库



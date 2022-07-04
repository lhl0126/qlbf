import requests
import time
import json
import random
import hashlib
import threading
import sys,os
import urllib3

'''
变量 jztt_phone_passwd=手机号&密码   多账号换行分割
'13317830426@lhl741023''
sig ='X2dk9sdnwoifPv7LuCTVhh4OEAU9v4MX'#line:1
urllib3 .disable_warnings ()#line:2
timestamp =str (int (time .time ()))#line:3
sig2 =sig +timestamp #line:4
sign =hashlib .md5 (sig2 .encode (encoding ='utf-8')).hexdigest ()#line:5
host ='https://api.st615.com'#line:7
money_sum ='0.3'#line:9
key ='seconds'#line:10
id =random .randint (2000000 ,3000000 )#line:11
r =random .randint (20 ,31 )#line:12
t =random .randint (1 ,3 )#line:13
def get_user (O0OO0O000O000000O ,OO00OOO0O000OOO0O ,O00OO000OO000O000 ):#line:14
    try :#line:15
        O00OOO0OO0OO000O0 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO00OOO0O000OOO0O ),'timestamp':str (O00OO000OO000O000 ),'token':str (O0OO0O000O000000O ),}#line:26
        print ("🔔九章头条,开始!")#line:27
        O00O0OOO000OOOOO0 =requests .get (url =f'{host}/v2/user/info?token={O0OO0O000O000000O}',headers =O00OOO0OO0OO000O0 ,verify =False )#line:28
        O0OOO0OOO0000O0OO =json .loads (O00O0OOO000OOOOO0 .text )#line:29
        OO0O00O0O0OO0O0OO =O0OOO0OOO0000O0OO ['code']#line:30
        if OO0O00O0O0OO0O0OO ==0 :#line:31
            OO00OO0000O0O00OO =O0OOO0OOO0000O0OO ['data']['money']#line:32
            OO0OOOOOOO0OO00O0 =O0OOO0OOO0000O0OO ['data']['integral']#line:33
            O0O0O00O00OOOOO0O =O0OOO0OOO0000O0OO ['data']['name']#line:34
            print ('用户名:%s'%(O0O0O00O00OOOOO0O ),'\n' '当前余额:%s'%(OO00OO0000O0O00OO ),'\n' '剩余金币:%s'%(OO0OOOOOOO0OO00O0 ))#line:35
            get_ziliao (O0OO0O000O000000O ,OO0OOOOOOO0OO00O0 ,OO00OOO0O000OOO0O ,O00OO000OO000O000 )#line:36
        else :#line:37
            print ("❌无效的token,请重新登录%s"%(O0OO0O000O000000O ))#line:38
    except :#line:39
        pass #line:40
def get_usertask (OOOO0O0OOOO000O00 ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO ):#line:41
    get_user (OOOO0O0OOOO000O00 ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:42
    O0O000OO0OOOOO0O0 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO0OO00OO0000O00O ),'timestamp':str (OOO00O0OOOOOOOOOO ),'token':str (OOOO0O0OOOO000O00 ),}#line:53
    O0OOO00O00O000000 =requests .get (url =f'{host}/v2/user/task?token={OOOO0O0OOOO000O00}',headers =O0O000OO0OOOOO0O0 ,verify =False )#line:55
    OO0O0OO00O0OOO00O =json .loads (O0OOO00O00O000000 .text )#line:56
    O0O0O0O00000OOOOO =OO0O0OO00O0OOO00O ['code']#line:57
    if O0O0O0O00000OOOOO ==0 :#line:58
        pass #line:59
    else :#line:60
        print ("❌无效的token,请重新填写")#line:61
    O000OO0OOOO0000OO =OO0O0OO00O0OOO00O ['data']['new_task'][0 ]['is_finish']#line:62
    if O000OO0OOOO0000OO ==1 :#line:63
        print ('📣新人首次阅读已完成')#line:64
    else :#line:65
        get_yuedu (OOOO0O0OOOO000O00 ,id ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:66
    OOOO00OO00000O0O0 =OO0O0OO00O0OOO00O ['data']['new_task'][3 ]['is_finish']#line:68
    O000OO0O0OO0OO00O =OO0O0OO00O0OOO00O ['data']['daily_task'][0 ]['is_finish']#line:70
    if O000OO0O0OO0OO00O ==0 :#line:71
        print ('📣阅读得最大奖励已完成')#line:72
    else :#line:73
        get_yuedu (OOOO0O0OOOO000O00 ,id ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:74
    OO00O00OOO0O00OOO =OO0O0OO00O0OOO00O ['data']['daily_task'][3 ]['is_finish']#line:75
    if OO00O00OOO0O00OOO ==1 :#line:76
        print ('📣阅读任务已完成')#line:77
    else :#line:78
        get_yuedu (OOOO0O0OOOO000O00 ,id ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:79
    OOOO0OOOOO00O00O0 =OO0O0OO00O0OOO00O ['data']['daily_task'][4 ]['is_finish']#line:81
    if OOOO0OOOOO00O00O0 ==1 :#line:82
        print ('📣转发文章已完成')#line:84
    else :#line:85
        get_zhuanfa (OOOO0O0OOOO000O00 ,id ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:87
    O00OOO0000O0OOOO0 =OO0O0OO00O0OOO00O ['data']['daily_task'][5 ]['is_finish']#line:88
    if O00OOO0000O0OOOO0 ==1 :#line:89
        print ('📣阅读5分钟已完成')#line:91
    else :#line:92
        get_yuedu (OOOO0O0OOOO000O00 ,id ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:94
    O00000OO00O000O00 =OO0O0OO00O0OOO00O ['data']['ads_task'][0 ]#line:95
    if (key in O00000OO00O000O00 ):#line:96
        print ('📣看视频1已完成')#line:98
    else :#line:99
        get_task (OOOO0O0OOOO000O00 ,8 ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:101
        print ("123")#line:103
    O0OO0OOOO000O00O0 =OO0O0OO00O0OOO00O ['data']['ads_task'][1 ]#line:104
    if (key in O0OO0OOOO000O00O0 ):#line:105
        print ('📣看视频2已完成')#line:107
    else :#line:108
        get_task (OOOO0O0OOOO000O00 ,9 ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:109
    O000O00000O0OO0O0 =OO0O0OO00O0OOO00O ['data']['ads_task'][2 ]#line:111
    if (key in O000O00000O0OO0O0 ):#line:112
        print ('📣看视频3已完成')#line:114
    else :#line:115
        get_task (OOOO0O0OOOO000O00 ,10 ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:116
    O00OOOOO0O00OO000 =OO0O0OO00O0OOO00O ['data']['ads_task'][2 ]#line:118
    if (key in O00OOOOO0O00OO000 ):#line:119
        print ('📣看视频3已完成')#line:121
    else :#line:122
        get_task (OOOO0O0OOOO000O00 ,11 ,OO0OO00OO0000O00O ,OOO00O0OOOOOOOOOO )#line:123
def get_code (OO0O0O0000O0OO0OO ,OO0OOOOOOOOO00O00 ,OO0OO00OO0000O000 ):#line:125
    O0O000O00O00O000O ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO0OOOOOOOOO00O00 ),'timestamp':str (OO0OO00OO0000O000 ),'token':str (OO0O0O0000O0OO0OO ),}#line:136
    OO0OOOOO00O000000 ={'token':OO0O0O0000O0OO0OO ,'code':'xxxx'}#line:138
    O00OO0000O00O0000 =requests .post (url =f'{host}/v2/user/bind',headers =O0O000O00O00O000O ,data =OO0OOOOO00O000000 ,verify =False )#line:139
def get_baoxiang (O00O0OO0O0O0OO0O0 ,OO0OOO0O0OOOO0OO0 ,O0O0000O00O00OOOO ):#line:141
    OOO00OO0OOO0O0O0O ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO0OOO0O0OOOO0OO0 ),'timestamp':str (O0O0000O00O00OOOO ),'token':str (O00O0OO0O0O0OO0O0 ),}#line:152
    print ('📣开始领取宝箱')#line:153
    OOO0OOOOO0OO00000 ={'token':O00O0OO0O0O0OO0O0 }#line:154
    O0000O000O0O00000 =requests .post (url =f'{host}/v2/task/receive',headers =OOO00OO0OOO0O0O0O ,data =OOO0OOOOO0OO00000 ,verify =False )#line:155
    O0OO0000O00OOOO0O =json .loads (O0000O000O0O00000 .text )#line:156
    O00O00O0000OOO00O =O0OO0000O00OOOO0O ['msg']#line:157
    if O00O00O0000OOO00O =='已领取，请到下个时间段继续领取哦~':#line:158
        print ("宝箱时间还未到")#line:159
        get_zhuanfa (O00O0OO0O0O0OO0O0 ,id ,OO0OOO0O0OOOO0OO0 ,O0O0000O00O00OOOO )#line:161
        pass #line:162
    else :#line:163
        print ("📣领取状态:%s"%(O00O00O0000OOO00O ))#line:164
        print ("等待继续领取三倍视频")#line:165
        get_task (O00O0OO0O0O0OO0O0 ,98 ,OO0OOO0O0OOOO0OO0 ,O0O0000O00O00OOOO )#line:166
def get_zhuanfa (OO00O000000O0OOO0 ,O00000OO0OO0OOO0O ,OO000O0O0O0O0OO00 ,OOO000OO00OOOO0O0 ):#line:168
    O00OO00O0O00O00OO ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO000O0O0O0O0OO00 ),'timestamp':str (OOO000OO00OOOO0O0 ),'token':str (OO00O000000O0OOO0 ),}#line:179
    print ('📣开始转发任务')#line:180
    OOO0OOO0OO0O00000 ={'token':OO00O000000O0OOO0 ,'source':'article','device':'android','os':',android','system':' Android','id':O00000OO0OO0OOO0O }#line:187
    O000O00OOOO00OO00 =requests .post (url =f'{host}/v2/article/share',headers =O00OO00O0O00O00OO ,data =OOO0OOO0OO0O00000 ,verify =False )#line:188
    OO00O000O0O0OO0OO =json .loads (O000O00OOOO00OO00 .text )#line:189
    O000O00O0OO0O00O0 =OO00O000O0O0OO0OO ['msg']#line:190
    print ('文章转发:%s'%(O000O00O0OO0O00O0 ))#line:191
def get_yuedu (OO0OOOOOOO000OOOO ,O000O0OO0O0O0O0O0 ,OO0OO000000000OOO ,OOOOOOOOO0OO0O000 ):#line:193
    for O00O00OOOO00O0O00 in range (20 ):#line:194
        OOO00000O0O000O00 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO0OO000000000OOO ),'timestamp':str (OOOOOOOOO0OO0O000 ),'token':str (OO0OOOOOOO000OOOO ),}#line:205
        OOOOO0OO00000OO0O ={'token':OO0OOOOOOO000OOOO ,'id':O000O0OO0O0O0O0O0 }#line:209
        O0O0O0000O00OO0O0 =requests .get (url =f'{host}/v2/article/detail?token={OO0OOOOOOO000OOOO}&id={O000O0OO0O0O0O0O0}',headers =OOO00000O0O000O00 ,verify =False )#line:210
        O0OOOOOO0000OO00O =requests .post (url =f'{host}/v2/article/finish',headers =OOO00000O0O000O00 ,data =OOOOO0OO00000OO0O ,verify =False )#line:211
        OOO00O0O0O00OOO0O =json .loads (O0OOOOOO0000OO00O .text )#line:212
    print ('📣完成阅读文章')#line:213
def get_task (OOO00000000O0OOO0 ,OOOOOO000O00O0OO0 ,OO0O00OO0OO00O000 ,OOOOOO0000OO0OO0O ):#line:215
    OO000OOO0O0OOO000 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO0O00OO0OO00O000 ),'timestamp':str (OOOOOO0000OO0OO0O ),'token':str (OOO00000000O0OOO0 ),}#line:226
    print ('📣开始看视频')#line:227
    O0O000OOOO000OO00 ={'token':OOO00000000O0OOO0 ,'id':OOOOOO000O00O0OO0 }#line:228
    O00O0O0O0000O0OO0 =requests .post (url =f'{host}/v2/task/ads',headers =OO000OOO0O0OOO000 ,data =O0O000OOOO000OO00 ,verify =False )#line:229
    OO0O0O000O00O0O0O =json .loads (O00O0O0O0000O0OO0 .text )#line:230
    OO0O0O0OO0000O0O0 =OO0O0O000O00O0O0O ['msg']#line:231
    print ('看视频金币%s:'%(OOOOOO000O00O0OO0 ),'%s'%(OO0O0O0OO0000O0O0 ),)#line:232
def get_tixian (OOO0OOO00000O0OO0 ,OO00000OOOO0OO0OO ,OO00000O0OO00O0O0 ,OOO000O0OOOOO0000 ):#line:234
    OOO0OO00000O0O0O0 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OO00000O0OO00O0O0 ),'timestamp':str (OOO000O0OOOOO0000 ),'token':str (OOO0OOO00000O0OO0 ),}#line:245
    print ('📣开始提现')#line:246
    O00O000000OO0O0OO ={'token':OOO0OOO00000O0OO0 ,'source':'article','device':'android','os':',android','system':' Android'}#line:252
    OOOO0O000OO0O0O00 ={'token':OOO0OOO00000O0OO0 ,'source':'article','type':'1','money':OO00000OOOO0OO0OO }#line:257
    for OOO00OO00O0OOO000 in range (4 ):#line:258
        O000000OO0O0OOOOO =requests .post (url =f'{host}/v2/article/share',headers =OOO0OO00000O0O0O0 ,data =O00O000000OO0O0OO ,verify =False )#line:259
        if OOO00OO00O0OOO000 ==3 :#line:260
            OO000OOO0000OOOOO =requests .post (url =f'{host}/v2/cash/withdraw-new',headers =OOO0OO00000O0O0O0 ,data =OOOO0O000OO0O0O00 ,verify =False )#line:261
            O00O0OOO0OO000O0O =json .loads (OO000OOO0000OOOOO .text )#line:262
            OOOOOO0OO00O0OOO0 =O00O0OOO0OO000O0O ['msg']#line:263
            print ('📣提现状态:%s'%(OOOOOO0OO00O0OOO0 ))#line:264
        else :#line:266
            print ('📣完成提现任务%s'%(OOO00OO00O0OOO000 ))#line:267
def get_ziliao (OOOOOO0O00OO0OOO0 ,OOOO00OOOO0O0000O ,O00OO0OO000OO0000 ,O0OOO00000OOOOOOO ):#line:269
    O00O00O0OO0OOOO0O ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (O00OO0OO000OO0000 ),'timestamp':str (O0OOO00000OOOOOOO ),'token':str (OOOOOO0O00OO0OOO0 ),}#line:280
    print ('📣开始完成资料任务')#line:281
    OO000OO00O0000O00 ={'token':OOOOOO0O00OO0OOO0 ,'avatar':'https://cdn.danzhiyeshentu.com/image/92/9237a2cbbc1e565b9b7cc2fcc0730c46.png','name':'用户_'+str (OOOO00OOOO0O0000O ),'avatar':'avatar','sex':'1','intro':str (OOOO00OOOO0O0000O ),'address':'北京市 北京市','birthday':'2020-01-02'}#line:290
    OOOOOOO000O0OO00O =requests .post (url =f'{host}/v2/user/edit',headers =O00O00O0OO0OOOO0O ,data =OO000OO00O0000O00 ,verify =False )#line:291
def get_daka (O0000OOOO0OO00O0O ,O0O0O00OOO0O00OOO ,OO00OO00O0OOOOOOO ):#line:293
    O0O00OOO0OOOO0O0O ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (O0O0O00OOO0O00OOO ),'timestamp':str (OO00OO00O0OOOOOOO ),'token':str (O0000OOOO0OO00O0O ),}#line:304
    OO0OOO0OOO00O0OO0 ={'is_double':'0',}#line:306
    OO0OOO0O0OO000000 =requests .post (url =f'{host}/v2/index/clock',headers =O0O00OOO0OOOO0O0O ,data =OO0OOO0OOO00O0OO0 ,verify =False )#line:307
    O00O0O00O00000O00 =json .loads (OO0OOO0O0OO000000 .text )#line:308
    OO0O0OO0OO00O00O0 =O00O0O00O00000O00 ['msg']#line:309
    print ('📣打卡任务%s'%(OO0O0OO0OO00O00O0 ))#line:310
def get_daka1 (O000OO0O0O00OOOO0 ,O00O0O00OO00O00O0 ,OOOOO00OO0O0O00OO ):#line:312
    O0O000OO0OOO000OO ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (O00O0O00OO00O00O0 ),'timestamp':str (OOOOO00OO0O0O00OO ),'token':str (O000OO0O0O00OOOO0 ),}#line:323
    OOO00OOOOO0O0O0OO ={'token':O000OO0O0O00OOOO0 }#line:325
    OO0OOO0OOO0OOO000 =requests .post (url =f'{host}/v2/task/continue',headers =O0O000OO0OOO000OO ,data =OOO00OOOOO0O0O0OO ,verify =False )#line:326
    O00OOOOOOOO0OOOO0 =json .loads (OO0OOO0OOO0OOO000 .text )#line:327
    OOO000O0000000O00 =O00OOOOOOOO0OOOO0 ['msg']#line:328
    print ('📣打卡视频任务%s'%(OOO000O0000000O00 ))#line:329
def get_qiandao (O00O0000OO00O000O ,O0OO00OO0O00OO000 ,O000O00O0OOOOOO0O ):#line:330
    O0OOO0OOO0O0OO0O0 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (O0OO00OO0O00OO000 ),'timestamp':str (O000O00O0OOOOOO0O ),'token':str (O00O0000OO00O000O ),}#line:341
    print ('📣开始签到')#line:342
    O0O0O0O0O0O0O00OO =requests .post (url =f'{host}/v2/sign/sign',headers =O0OOO0OOO0O0OO0O0 ,verify =False )#line:343
    O0000O000O00000OO =json .loads (O0O0O0O0O0O0O00OO .text )#line:344
    O0O0O0O0O000O0OOO =O0000O000O00000OO ['msg']#line:345
    print ('签到状态:%s'%(O0O0O0O0O000O0OOO ))#line:346
def get_shouye (OOO0OOO00O00OO0OO ,OOOO000O00000O00O ,O0O0O00O00OO000OO ):#line:348
    O00OO0O00OO0O0000 ={'User-Agent':'ChapterNine/1.2.8 (com.ass.jiuzhang; build:1137; iOS 12.2.0) Alamofire/5.4.4','Accept':'*/*','Connection':'keep-alive','Accept-Encoding':'br;q=1.0, gzip;q=0.9, deflate;q=0.8','noncestr':'uCTVhh4OEAU9v4MX','Accept-Language':'zh-Hans-CN;q=1.0','sign':str (OOOO000O00000O00O ),'timestamp':str (O0O0O00O00OO000OO ),'token':str (OOO0OOO00O00OO0OO ),}#line:359
    OO0OO00O0O0O00OO0 =requests .get (url =f'{host}/v2/index/get-benefit?token={OOO0OOO00O00OO0OO}',headers =O00OO0O00OO0O0000 ,verify =False )#line:360
    OOO00OO000OOO0000 =json .loads (OO0OO00O0O0O00OO0 .text )#line:361
    O0000OO00O0OO0000 =OOO00OO000OOO0000 ['msg']#line:362
    print ('📣首页金币任务%s'%(O0000OO00O0OO0000 ))#line:363
    get_task (OOO0OOO00O00OO0OO ,77 ,OOOO000O00000O00O ,O0O0O00O00OO000OO )#line:364
def main (OO0O0O0000O0O0000 ):#line:365
    O0O0O000OO000O0O0 =threading .Thread (target =get_usertask ,args =(OO0O0O0000O0O0000 ,sign ,timestamp ,))#line:367
    O0O0O000OO000O0O0 .start ()#line:368
    O00O00OO00O0O000O =threading .Thread (target =get_qiandao ,args =(OO0O0O0000O0O0000 ,sign ,timestamp ,))#line:369
    O00O00OO00O0O000O .start ()#line:370
    O00O0OO0O0O0O00OO =threading .Thread (target =get_shouye ,args =(OO0O0O0000O0O0000 ,sign ,timestamp ,))#line:371
    O00O0OO0O0O0O00OO .start ()#line:372
    O0O0O0O00OOOOOO0O =threading .Thread (target =get_daka ,args =(OO0O0O0000O0O0000 ,sign ,timestamp ,))#line:373
    O0O0O0O00OOOOOO0O .start ()#line:374
    OO0O0OO0000OOO0OO =threading .Thread (target =get_task ,args =(OO0O0O0000O0O0000 ,73 ,sign ,timestamp ,))#line:375
    OO0O0OO0000OOO0OO .start ()#line:376
    OO00000O00OO0O0OO =threading .Thread (target =get_task ,args =(OO0O0O0000O0O0000 ,71 ,sign ,timestamp ,))#line:377
    OO00000O00OO0O0OO .start ()#line:378
    OO00000O00OO0O0OO =threading .Thread (target =get_task ,args =(OO0O0O0000O0O0000 ,94 ,sign ,timestamp ,))#line:379
    OO00000O00OO0O0OO .start ()#line:380
    O0OO000O0OO0OOO00 =threading .Thread (target =get_baoxiang ,args =(OO0O0O0000O0O0000 ,sign ,timestamp ,))#line:381
    O0OO000O0OO0OOO00 .start ()#line:382
    OOOOOOO0000OO00OO =threading .Thread (target =get_tixian ,args =(OO0O0O0000O0O0000 ,money_sum ,sign ,timestamp ,))#line:383
    OOOOOOO0000OO00OO .start ()#line:384
    O0OO000O0OO0OOO00 =threading .Thread (target =get_yuedu ,args =(OO0O0O0000O0O0000 ,id ,sign ,timestamp ,))#line:385
    O0OO000O0OO0OOO00 .start ()#line:386
    print ('🔔所有线程已启动！')#line:387
'''  
def denglu(phone,passwd):
    try:
        headers = {
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'pragma': 'no-cache',
            'Content - Type': 'application / x - www - form - urlencoded',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; HUAWEI Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 JIUZHANG/android Html5Plus/1.0 (Immersed/36.57143)',
        }
        print('开始登陆:%s' % (phone),)
        data = {
            " device ": "iPhone",
            " invite": "0",
            "jpush_id": "",
            " mobile": str(phone),
            " news_id": "",
            "os": "12.2 ",
            "password": passwd,
            " uuid ": "",
            " version": "1.2.5"}
        response = requests.post(url='https://api.st615.com/api/oauth/login', headers=headers, data=data)
        Obtain = json.loads(response.text)
        qianming = Obtain['data']['token']
        return qianming
    except:
        pass
'''#line:416
def denglu (OO0O00O00O0OO00OO ,O00000OOOO000OO00 ,OOOO0O0000O0O000O ,OOOOOOO000O0OO000 ):#line:419
        OOOO000OOO000O00O ={'sign':OOOO0O0000O0O000O ,'noncestr':'C2YSyOQjaZ48H64l','timestamp':OOOOOOO000O0OO000 ,'Content-Type':'multipart/form-data; boundary=5b0d01ac-6d14-4d52-9fd7-868c803fb13a','Content-Length':'1492','Host':'api.st615.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.10.0','Cache-Control':'no-cache'}#line:431
        print ('开始登陆:%s'%(OO0O00O00O0OO00OO ),)#line:432
        O0O00000O000O0OOO ='''
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="password"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 9

{}
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="jpush_id"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 19

160a3797c8f081e69c4
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="os"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 9

Android12
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="mobile"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 11

{}
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="uuid"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 16

596f361e13411998
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="device"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 13

OnePlusIN2020
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a
Content-Disposition: form-data; name="version"
Content-Transfer-Encoding: binary
Content-Type: multipart/form-data; charset=utf-8
Content-Length: 5

2.1.7
--5b0d01ac-6d14-4d52-9fd7-868c803fb13a--
        
'''.format (O00000OOOO000OO00 ,OO0O00O00O0OO00OO )#line:485
        OO0000OO00OO00000 =requests .post (url ='https://api.st615.com/api/oauth/login',headers =OOOO000OOO000O00O ,data =O0O00000O000O0OOO ,verify =False )#line:486
        OO00O000OO000O0O0 =json .loads (OO0000OO00OO00000 .text )#line:487
        OOO0O00OO0O0O0O00 =OO00O000OO000O0O0 ['data']['token']#line:488
        return OOO0O00OO0O0O0O00 #line:489
def phone_passwd ():#line:493
    if "jztt_phone_passwd"in os .environ :#line:494
        OO0OOOOOOO000OO00 =os .environ ['jztt_phone_passwd'].split ('\n')#line:495
        if len (OO0OOOOOOO000OO00 )>0 :#line:496
            return OO0OOOOOOO000OO00 #line:497
        else :#line:498
            print ("jztt_phone_passwd变量未启用")#line:499
            sys .exit (1 )#line:500
    else :#line:501
        print ("未添加jztt_phone_passwd变量")#line:502
        sys .exit (0 )#line:503
if __name__ =='__main__':#line:505
    phone_passwd_all =phone_passwd ()#line:507
    for i in phone_passwd_all :#line:508
        phone =i .split ('&')[0 ]#line:509
        passwd =i .split ('&')[1 ]#line:510
        token =denglu (phone ,passwd ,sign ,timestamp )#line:511
        if token ==None :#line:512
            print ("账号密码错误")#line:513
        else :#line:514
            main (token )#line:515

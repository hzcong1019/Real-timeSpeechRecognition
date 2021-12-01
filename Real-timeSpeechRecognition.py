# coding:utf-8

"""
实时语音识别
"""
import speech_recognition as sr
import logging
import os
from munch import Munch
import winsound
import win32com.client as w32
import requests
import json

logging.basicConfig(level=logging.INFO)
speak_out = w32.Dispatch('SAPI.SPVOICE')


# 图灵机器人获取回复消息
def talks_robot(info='hello world'):
    # 图灵机器人api接口
    api_url = 'http://www.tuling123.com/openapi/api'
    # 这里替换你的图灵api密钥
    api_key = 'xxx'
    data = {'key': api_key,
            'info': info}
    # 通过接收消息info,对数据在封装，向灵图机器人发出请求请求，并获得回复
    req = requests.post(api_url, data=data).text
    # loads方法是把json对象转化为python对象，dumps方法是把pyhon对象转化为json对象
    replys = json.loads(req)['text']
    return replys  # 返回回复数据


while True:
    r = sr.Recognizer()
    # 麦克风
    mic = sr.Microphone()
    logging.info('录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    logging.info('录音结束，识别中...')
    # 如果你的网络没有科学上网，这里因为网络问题会报错,进去方法修改谷歌的url，把com改为cn
    result = r.recognize_google(audio, language='cmn-Hans-CN', show_all=True)
    munch = Munch.fromDict(result)
    print(munch)
    # 结果为空则不进行处理
    if munch:
        # 提取第0个文本，confidence最高
        text = munch.alternative[0].transcript
        # 这是os相关操作示例，大家可以自行添加关键字
        if text == '打开微信':
            speak_out.Speak('正在打开微信……')
            # 这里的路径要填对哦
            os.startfile('D:\Program Files (x86)\Tencent\WeChat\WeChat.exe')
        elif text == '关闭微信':
            speak_out.Speak('正在关闭微信……')
            os.system('taskkill /F /IM WeChat.exe')
        elif text == '打开QQ':
            speak_out.Speak('正在打开QQ……')
            # 这里的路径要填对哦
            os.startfile('C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe')
        elif text == '关闭QQ':
            speak_out.Speak('正在关闭QQ……')
            os.system('taskkill /F /IM QQ.exe')

        # 这里是机器人部分
        else:
            # 文本传给机器人拿到返回值
            reply = talks_robot(text)
            print('机器人说：', reply)
            # 让程序开口说话
            speak_out.Speak(reply)
            winsound.PlaySound('ALARM8', winsound.SND_ASYNC)

    logging.info('end')

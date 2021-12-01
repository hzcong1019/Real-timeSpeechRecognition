# Real-timeSpeechRecognition
实时语音识别

该项目需要用到的库

```python
speech_recognition
os
Munch
win32com.client
requests
```

两个安装名字不一样重点说下，其他均可通过pip安装

1.安装speech_recognition

```python
pip install SpeechRecognition
```

如果安装不了可以用百度镜像

```python
pip install SpeechRecognition -i https://mirror.baidu.com/pypi/simple
```

2.安装win32com.client

```python
pip install pywin32
```

3.运行可能会报的错

```
AttributeError: Could not find PyAudio; check installation
```

尝试安装PyAudio

正常pip install PyAudio好像不行，会报错。可以尝试以下方法：

```
pip install pipwin
pipwin install PyAudio
```

运行起来如果识别报错

```
speech_recognition.RequestError: recognition connection failed: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
```

这是因为使用的是谷歌的语音识别接口，可以进去recognize_google方法，找到url

```
url = "http://www.google.com/speech-api/v2/recognize?{}"
```

把com改成cn

```
url = "http://www.google.cn/speech-api/v2/recognize?{}"
```

关于机器人使用的是图灵机器人，大家可以注册一个图灵机器人，把key改成自己的key。

[点击进入图灵机器人官网](http://www.turingapi.com/)

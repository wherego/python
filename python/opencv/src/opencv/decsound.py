
#coding=utf-8
import wave
import pylab as pl
import numpy as np
# 打开WAV文档
print "open wav files...."
f1 = wave.open(r"t.wav", "rb")
f2 = wave.open(r"t.wav", "wb")
# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
print "read wav data...."
params = f1.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# 读取波形数据
str_data = f1.readframes(nframes)
#将波形数据转换为数组，并更改，减少音量

print "update wav data...."
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data =wave_data/100
str_data=wave_data.tostring()
#写波形数据参数
print "save new wav files...."
f2.setnchannels(nchannels)
f2.setframerate(framerate)
f2.setsampwidth(sampwidth)
f2.writeframes(str_data)
print "close  wav files...."
f2.close()
f1.close()
import python.wave2ivec as w2i
import os
import librosa
import numpy as np


def concatenate(ids, t):
    fs = 22050
    for i in ids:
        print(i)
        path = "./wav/" + i
        folders = os.listdir(path)
        data = np.array([], dtype='float32')
        for j in folders:
            files = os.listdir(path + '/' + j)
            for k in files:
                filePath = path + '/' + j + '/' + k
                print(filePath)
                if len(data) >= (t+5)*fs:
                    print("hello")
                    break
                else:
                    sig, fs = librosa.load(filePath, mono=True)
                    data = np.append(data, sig)
            if len(data) >= (t+5)*fs:
                break
        if len(data) < (t+5)*fs:
            print("oj joj")
        savePath = "./in/test/" + i + ".wav"
        librosa.output.write_wav(savePath, data[0:(5*fs-1)], 22050)
        savePath = "./in/train/90/" + i + ".wav"
        librosa.output.write_wav(savePath, data[(5*fs):((t+5)*fs-1)], 22050)


def divideTrainFiles(start, stop, step):
    trainFiles = os.listdir("./in/train/90")

    for j in range(start, stop, step):
        os.makedirs("./in/train/" + str(j))

    for i in trainFiles:
        path = "./in/train/90/" + i
        sig, fs = librosa.load(path, mono=True)
        for j in range(start,stop,step):
            save_path = "./in/train/" + str(j) + "/" + i
            librosa.output.write_wav(save_path, sig[0:(j*fs-1)], fs)


ids = os.listdir("./wav")
# concatenate(ids,90)
divideTrainFiles(5,90,5)

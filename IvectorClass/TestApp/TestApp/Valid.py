import python.wave2ivec as w2i
import os
import numpy as np


def createIvectors(i_vector):
    test_files = os.listdir("./in/test")
    train_folders = os.listdir("./in/train")

    for i in train_folders:
        path = "./in/train/" + i
        train_files = os.listdir(path)
        for j in train_files:
            print(j)
            readPath = path + "/" + j
            w, n_data = i_vector.process_wav(readPath)
            i_vector.save_ivector_to_file("./out/train/" + i + "/" + j + ".ivec", w, n_data)

    for i in test_files:
        print(i)
        readPath = "./in/test" + "/" + i
        w, n_data = i_vector.process_wav(readPath)
        i_vector.save_ivector_to_file("./out/test/" + i + ".ivec", w, n_data)


def score(i_vector):
    out_train_folders = os.listdir("./out/train")

    for i in out_train_folders:
        s = i_vector.get_score_from_ivectors("./out/train/" + i, "./out/test")
        print(type(s))
        np.save("./out/score/" + i, s)


def load():
    out_score_files = os.listdir("./out/score")

    for i in out_score_files:
        s = np.load("./out/score/" + i)
        print(s)


# i_vector = w2i.IVector()
# createIvectors(i_vector)
# score(i_vector)
load()


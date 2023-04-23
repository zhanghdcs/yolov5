from genericpath import exists
import os, random, shutil

def moveFile(fileDir, tarDir):
        pathDir = os.listdir(fileDir)    #取图片的原始路径
        if not os.path.exists(tarDir):
            os.mkdir(tarDir)
        # filenumber=len(pathDir)
        # rate=0.1    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
        # picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
        picknumber=500#按照rate比例从文件夹中取一定数量图片
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
        # print (sample)
        fo = open("dataset_daytime_500.txt", "w")
        for name in sample:
            shutil.move(fileDir+name, tarDir+name)
            # fo = open("dataset.txt", "w")
            fo.write(str(tarDir+name) + "\n")
        fo.close()
        return

if __name__ == '__main__':
   fileDir = "./data/3D_mix_dataset/images/train/"    #源图片文件夹路径
   tarDir = './wushibie_3D/'    #移动到新的文件夹路径
   moveFile(fileDir, tarDir)

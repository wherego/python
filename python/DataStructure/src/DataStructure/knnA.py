#-*- coding: utf-8 -*-
from numpy import *
import operator

'''构造数据'''
def createDataSet():
    characters=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return characters,labels

def classify(sample,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]     #数据集行数即数据集记录数
    '''距离计算'''
    diffMat=tile(sample,(dataSetSize,1))-dataSet         #样本与原先所有样本的差值矩阵
    sqDiffMat=diffMat**2      #差值矩阵平方
    sqDistances=sqDiffMat.sum(axis=1)       #计算每一行上元素的和
    distances=sqDistances**0.5   #开方
    sortedDistIndicies=distances.argsort()      #按distances中元素进行升序排序后得到的对应下标的列表
    '''选择距离最小的k个点'''
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    '''从大到小排序'''
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def main():
    sample=[0,0]
    k=3
    group,labels=createDataSet()
    label=classify(sample,group,labels,k)
    print("Classified Label:"+label)

if __name__=='__main__':
    main()
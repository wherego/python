import math

class sort:
    def selectSort(self,L):
        size = len(L)
        for i in range(0,size):
            max=L[i]
            index = i
            for j in range(i,size):
                if L[j] > max:
                    max=L[j]
                    index=j
            temp = L[i]
            L[i]=max
            L[index]=temp
            print(L)
    def insertSort(self,L):
        size = len(L)
        for i in range(1,size):
            fv = L[i]
            j = i
            while(j>=1):
                if fv < L[j-1]:
                    L[j] = L[j-1]
                else:
                    break
                j=j-1
            L[j] = fv
            print(L)
    def bubbleSort(self,L):
        size = len(L)
        for i in range(size-1,-1,-1):
            for j in range(0,i-1):#������Ҫע���£����¿����Ƿ���ϣ��о��ֵֹ�
                if L[j]>L[j+1]:
                    temp = L[j]
                    L[j]=L[j+1]
                    L[j+1] = temp
            print(L)

    def merge(self,L1,L2):
        L=[]
        index1 = 0
        index2 = 0
        size1 = len(L1)
        size2 = len(L2)
        top = min(size1,size2)
        while(index1!=size1 and index2!=size2 ):
            if L1[index1] > L2[index2]:
                L.append(L2[index2])
                index2 = index2 + 1
            else:
                L.append(L1[index1])
                index1 = index1 + 1
        if index1 < size1:
            for i in range(index1,size1):
                L.append(L1[i])
        if index2 < size2:
            for i in range(index2,size2):
                L.append(L2[i])
        return L
    def mergeInL(self,L,first,mid,last):
        tempa = []
        tempb = []
        for i in range(first,mid+1):
            tempa.append(L[i])
        for i in range(mid+1,last+1):
            tempb.append(L[i])
        tempc = self.merge(tempa,tempb)
        index = 0
        for i in range(first,last+1):
            L[i] = tempc[index]
            index += 1
    #�Ҵ��ˡ�������������������д��д�ű����������������ٸ�
    def mergeSort(self,L,first,last):
        #print("1first = %d  last = %d" %(first,last))
        if first < last:
            #print("2first = %d  last = %d"%(first,last))
            mid = math.trunc((first+last)/2) #�����õ�����,����
            self.mergeSort(L,first,mid)
            self.mergeSort(L,mid+1,last)
            self.mergeInL(L,first,mid,last)
    #������Ч�ʸ�~~����ʵ�ָĽ����
    def quickSort(self,L,left,right):
        i = left
        j = right
        middle = L[left]
        while i<=j:
            while L[i]<middle and i<right:
                i += 1
            while L[j]>middle and j>left:
                j -= 1
            if i<=j: #����һ��
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                i += 1
                j += 1
        if left<j:
            self.quickSort(L,left,j)
        if right > i:
            self.quickSort(L,i,right)
    def __bucketInit(self):
        l0 = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        l7 = []
        l8 = []
        l9 = []
        bucket = [l0,l1,l2,l3,l4,l5,l6,l7,l8,l9]
        return bucket
    #��������
    def radixSort(self,L):
        radix = 10
        base = 1

        bucket = self.__bucketInit()
        max = L[0]
        for i in L:
            if i > max:
                max = i
        while math.trunc((max%radix)/base) > 0:
            #�ŵ�Ͱ��
            for i in L:
                index = math.trunc((i%radix)/base)
                bucket[index].append(i)
            #���������L
            L = []
            for i in bucket:
                L.extend(i)
            bucket = self.__bucketInit()
            print(L)
            #��һ��ѭ��ȡ��һλ
            radix *= 10
            base *=10
        return L
    #��������
    def countSort(self,L):
        size = len(L)
        min = max = L[0]
        #�õ�������С
        for i in L:
            if i<min:
                min = i
            if i>max:
                max = i
        #�õ����ֵ�����
        bound = max - min +1
        #��ʼ����������
        count =[]
        for i in range(0,bound):
            count.append(0)

        #ͳ��ÿ�������ֵĴ������ŵ�count��
        for i in range(0,size):
            count[ L[i]-min ] +=1

        z = 0
        print("min = %d and max = %d"%(min,max))
        for i in range(min,max+1):
            #print("i="+str(i))
            for j in range(0,count[i-min]):#count[i-min]��ʾ�����ֳ��ִ�����0�εػ���������εĻ����β���
                #print("j="+str(j))
                L[z] = i
                print(L)
                z+=1
        print(L)












a = sort()
l = [3,2,5,7,1,9]
print('ԭʼ����')
print(l)
print('ѡ������')
a.selectSort(l)
l2 = [3,2,5,7,1,9]
print('��������')
a.insertSort(l2)
print('ð������')
l3 = [3,2,5,7,1,9]
a.bubbleSort(l3)

print('�б�鲢�㷨 û������')
la = [1,3,5,7,9,11]
lb = [2,4,6,8]
print(a.merge(la,lb))
print('�鲢����')
lm = [3,2,5,7,1,9]
a.mergeSort(lm,0,5)
print(lm)
print('��������')
lq = [3,2,5,7,1,9]
a.quickSort(lq,0,5)
print(lq)
print('��������')
lr = [3,20,5,713,1,9]
print(lr)
a.radixSort(lr)
print("��������")
lz = [3,2,5,7,1,9]
a.countSort(lz)
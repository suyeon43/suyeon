''' ls = [10,20,30,40]
print('ls :',ls)
print('ls[0] : %d'%ls[0])
print('ls[1] : {}'.format(ls[1]))
print('ls[2] :',ls[2])
print('ls[3] :',ls[3]) '''

''' ls = [0,0,0,0]; Sum = 0
print('len(ls) :',len(ls))
for i in range(len(ls)):
    ls[i] = int(input(str(i)+'번 인덱스에 입력 : '))
print("ls :",ls)
for i in range(len(ls)):
    print('ls[%d] : %d'%(i,ls[i]))
    Sum += ls[i]
print('리스트 내부 값들의 합 :',Sum) '''

''' dd = [10,'test',1.123]
for i in range(len(dd)):
    print('dd[%d] :'%i,dd[i],end=' => ')
    print('type : %s'%type(dd[i])) '''

''' ls = [10,20,30,40]
print('ls :',ls)
print('ls[1:3] => ls[1] ~ [2] :',ls[1:3])
print('ls[0:3] => ls[0] ~ [2] :',ls[0:3])
print('ls[2:] => ls[2] ~ 끝까지 :',ls[2:])
print('ls[:2] => ls[0] ~ ls[1] :',ls[:2]) '''

''' a = 10
b = a
b = 20
print(a,b) '''

''' ls = [10,20,30,40]
arr = ls
arr[2] = 20000
print('ls :',ls,'ls id :',id(ls))
print('arr :',arr,'arr id :',id(arr)) '''

''' ls = [10,20,30,40]
arr = ls[:]
arr[2] = 20000
print('ls :',ls,'ls id :',id(ls))
print('arr :',arr,'arr id :',id(arr)) '''

''' import copy
ls = [10,20,30,40]
arr = copy.deepcopy(ls)
arr[2] = 20000
print('ls :',ls,'ls id :',id(ls))
print('arr :',arr,'arr id :',id(arr)) '''

''' from copy import deepcopy
ls = [10,20,30,40]
arr = deepcopy(ls)
arr[2] = 20000
print('ls :',ls,'ls id :',id(ls))
print('arr :',arr,'arr id :',id(arr)) '''

''' ls = [10,20,30]; arr = [40,50,60]
print('ls :',ls,'\narr :',arr)
st1 = ls + arr
print('ls + arr => st1 :',st1)
st2 = ls * 3
print('ls * 3 => st2 :',st2) '''

''' ls = [10,20,30]; arr = [40,50,60]
print('ls :',ls,'\narr :',arr)
st1 = [0,0,0]
for i in range(len(st1)):   st1[i] = ls[i] + arr[i]
print('ls + arr => st1 :',st1)
st2 = [0,0,0]
for i in range(len(st2)):   st2[i] = ls[i] * 3
print('ls * 3 => st2 :',st2) '''

''' ls = [10,20,30]
ls.append(1000)
for i in range(len(ls)):
    print('ls[%d] : %d'%(i,ls[i]))
print('리스트의 총 개수 :',len(ls))
print('ls :',ls)
ls = []
print('ls초기화 후 :',ls) '''

''' ls = []; Sum = 0
num = int(input('리스트의 데이터 개수 : '))
for i in range(num):
    a = int(input(str(i)+'번 인덱스 데이터 : '))
    ls.append(a)
print('ls :',ls) '''

''' ls = [30,20,10]
print('현재 리스트 :',ls)
ls.append(40)
print('append(40) 후의 리스트 :',ls)
print('pop()으로 추출한 값 :',ls.pop())
print('pop() 후의 리스트 :',ls)
ls.sort()
print('sort() 후의 리스트 :',ls)
ls.reverse()
print('reverse() 후의 ls :',ls)
del(ls[2])
print('del() 후의 리스트 :',ls) '''

''' ls = [30,20,10]
print('현재 리스트 :',ls)
print('10 값의 위치 :',ls.index(10))
ls.insert(2,200)
print('insert(2,200) 후의 리스트 :',ls)
ls.remove(200)
print('remove(200) 후의 리스트 :',ls)
ls.extend([555,666,555])
print('extend([555,666,555]) 후의 리스트 :',ls)
print('555 값의 개수 :',ls.count(555)) '''

'''
    ls = [10,5,20,7,9,31,12,11,19,32]
    
    실습 1
    빈 리스트 3개를 만들어서 ls의 데이터를 인덱스 번호를 기준으로 홀수번째의 값,
    짝수번째의 값을 따로 넣고, 짝수번째와 홀수번째 요소들의 차를 세번째 리스트에 넣어서 출력
    (결과는 [5, 13, -22, 1, -13] 이 나와야 합니다)

    실습 2
    ls의 요소 중 인덱스를 기준으로 홀수번째와 짝수번째 값들의 합을 각각 구하고
    그 둘의 합과 차를 출력
    (결과는 156, -16 이 나와야 합니다)
     * 실습 1에서 작성한 코드는 주석 걸고 진행

    실습 3
    ls에 저장된 값을 invertLs에 거꾸로 저장 후 출력
    ls의 값을 오름차순으로 sortLs에 저장 후 출력
    ls의 값을 내림차순으로 reverseLs에 저장 후 출력
    (결과는 ls를 포함한 4개의 리스트를 한번에 출력해서 확인해주세요)
'''
#ls = [10,5,20,7,9,31,12,11,19,32]
''' # 실습 1
odd,even,result = [],[],[]
for i in range(len(ls)):
    if i % 2 == 0:
        even.append(ls[i])
    else:
        odd.append(ls[i])
#print(odd, even)
for i in range(len(odd)):
    #result.append(even[i] - odd[i])
    a = even[i] - odd[i]
    result.append(a)
print(result) '''

''' # 실습 2
evenSum, oddSum, res1, res2 = 0,0,0,0
for i in range(len(ls)):
    if i % 2 == 0:
        evenSum += ls[i]
    else:
        oddSum += ls[i]
res1 = evenSum + oddSum
res2 = evenSum - oddSum
print('합 :',res1,'\n차 :',res2) '''

# 실습 3
''' from copy import deepcopy
invertLs = deepcopy(ls)
invertLs.reverse()
sortLs = deepcopy(ls)
sortLs.sort()
reverseLs = deepcopy(ls)
reverseLs.sort(reverse=True)
#reverseLs.sort()
#reverseLs.reverse()
print('ls\t\t:',ls,'\ninvertLs\t:',invertLs,'\nsortLs\t\t:',sortLs,'\nreverseLs\t:',reverseLs) '''

''' aa = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print('aa[0][0] :',aa[0][0])
print('aa[0][1] :',aa[0][1])
print('aa[0][2] :',aa[0][2])
print('aa[0][3] :',aa[0][3])
print('aa[1][0] :',aa[1][0])
print('aa[1][1] :',aa[1][1]) '''

''' import random
i = 0
for i in range(5):
    print(i,':',random.random()) '''

''' import random
i = 0
for i in range(5):
    print(i,':',int(random.random()*100)) '''

''' import random
for i in range(5):
    print(i,':',random.randrange(0,100)) '''

''' tp = (10,20,30)
print('tp :',tp)
print('tp type :',type(tp))
print('tp len :',len(tp)) '''

''' tp = 10,20,30
print('tp :',tp)
print('tp type :',type(tp))
print('tp[0] :',tp[0])
print('tp[0] type :',type(tp[0]))
tp[0] = 100 '''

''' tp = '문자열',100,1.111
print('tp :',tp)
print('type :',type(tp))
print('tp[0] type :',type(tp[0])) '''

''' tpInt = (10)
print('tpInt :',type(tpInt))
tpT1 = (10,)
print('tpT1 :',type(tpT1))
tpT2 = 10,
print('tpT2 :',type(tpT2)) '''
import random
import csv
# 평점 : 1~10 난수
# 사람 : 행
# 영화 종류 : 열
# 이중리스트로 결과값을 출력합니다
# 수정 배포 자유입니다. 출처만 남겨주세요

def ranmake (x,y):
    row = [] #열(겉의리스트)
    for i in range(x) :
        col = [] #안의 리스트
        col.append([random.randint(1,10) for k in range(y)]) #난수 생성 내장 랜덤함수는 리스트로 출력되서 밑에처럼 풀어줘야함
        #  .sample()은 유니크함 인풋이 시퀀스고 오직 인풋값 범위내의 len(10-1)의 값만 출력된다.
        f = sum(col, []) #2차원 리스트를 1차원으로 만들기 https://programmers.co.kr/learn/courses/4008/lessons/12738
        # []내의 함수를 각각 더해서 출력
        row.append(f)
    return row
# print("점수가 후한 30% 중간 30% 후 ")
print("얼마나 많은 사람이 몇개의 영화를 평가했을가요? 영화 사람 순으로 입력해주세요")
#영화는 열 x row
#사람은 행 y col
x = int(input())
y = int(input())
z = ranmake(x,y)
print(z)

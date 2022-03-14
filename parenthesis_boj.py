import sys

# input = sys.stdin.read()
#
# def valid_parent(str):
#     stack = []
#     cnt = 0
#     if p == '(':
#         cnt += 1
#     else:
#         cnt -=1
#     if cnt == 0:
#         print('yes')
#     else:
#         print('no')
#전체 테스트 케이스 수
T = int(input())

#테스트 케이스 동안
for i in range(T):
    p = input()#인풋 받기
    p_list = list(p)# 잘라서 리스트에 넣기
    print(p_list)
    cnt = 0 # 카운트 초기화
    #리스트에서 하나씩 꺼내서 비교
    for s in p_list:
        if s == '(':
            cnt += 1
        elif s == ')':
            cnt -= 1
        # 맨 처음부터 ')' 이면 볼 것도 없다
        if cnt < 0:
            print('no')
            break
    # 처음이 '(' 인 애들은
    if cnt == 0:
        print('yes')
    else:
        print('no')


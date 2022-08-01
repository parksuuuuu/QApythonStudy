#for문을 사용해 1부터 100까지의 자연수 중 입력한 값 배수의 합을 구해 보자.

result = 0
def add_number(args):
    result = 0
    for i in range (1, 101):    #문제에서 주어진 대로 for문을 사용하여 1부터 100까지 1회씩 반복
        if(i % args == 0):      #입력값을 argument로 받아 1~100중 입력값을 나눈 나머지가 0인지 비교
            result += i         #나머지가 0이면 입력값의 배수이기 때문에 result 변수에 합산 
            print(f"{i}는 {args}의배수")
        else:
            continue
    return result               #합산값 반환

num = int(input("배수를 입력하세요: "))
result=add_number(num)
print(f"1부터 100중 {num}배수의 총 합산 값 : {result}")

#################미완성입니다.####################################



#nums : 입력숫자
#val : 제거 숫자
#expectedNums : 예측된 답안
def removeElement(nums, val):
    count = 0
    for i in range(0,len(nums)):
        if  nums[i] != val:
            count = count +1
    return count

def solution(nums , val):
    expectedNums=[]
    newNums = []
    k = removeElement(nums, val)
    for i in range(0,len(nums)):
        if nums[i] == val:
            expectedNums.append("_")
        else :
            expectedNums.append(nums[i])
    return k, expectedNums
    
    
print(solution([0,1,2,2,3,0,4,2],2))
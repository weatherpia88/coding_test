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
    #print(nums,val)
    k = removeElement(nums, val)
    #print(k)
    for i in range(0,len(nums)):
        if nums[i] == val:
            expectedNums.append("_")
        else :
            expectedNums.append(nums[i])
    #print(expectedNums)
    count_ = 1
    for i in range(len(expectedNums)):
        #print(expectedNums[k-1])
        if i > k-2:
           if expectedNums[i] != '_':
              newNums.append(expectedNums[i])
        else:
            count_ = count_ + 1
         
    for i in range(0,count_):        
        newNums.append('_')
    return k, newNums
    
        
print(solution([3,2,2,3],3))

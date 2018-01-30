#The min_subarray_finder just calls and returns the value of min_subarray_finder_helper.
#min_subarray_finder_helper function returns the starting element of the given array in a list form
#if the length of the given array is equal to 1 or given start index is greater or
#equal to given end index. If not, it calculates the median index and calls itself by
#giving the corresponding parameters to itself. This way it splits the array to 2 halfs from the middle.
#Then it calls MiddleMin function.
#MiddleMin function starts from the given middle index and moves towards end and start indexes.
#It calculates the sum while iterating and stores its value and the
#starting and ending indexes if it is smaller than the minimum found before.
#We need to use this because the min_subarray_finder_helper is only capable of finding minimums if the
#minimum subarray is between middle and end or between middle and start. If we were looking for only a single
#element we wouldn't need it but not in this case since the subarray could have elements from both halves.
#It returns a subarray between the left and right indexes that gives the minimum sum.
#Since this is a Divide&Conquer algorithm its time complexity can be calculated with Master Method.
#Master method : T(n)=aT(n/b)+f(n) where a is the number of subproblems,n/b is the size of
#those problems and f(n) is the cost of combining them. In this  case we split the array into 2 halves
#with a size of n/2 therefore T(n)=2T(n/2)+O(n).
#Another way to explain this: 2T(n/2) since there are 2 recursive calls with a given array size of n/2
#MiddleMin function takes O(n) time since it iterates through the whole array starting from middle.
#This algorithm is also very similar to MergeSort and it has the same time complexity of
#T(n)=2T(n/2)+O(n) which can be solved with Master Theorem case 2 to find the result which is
#O(nlogn).
import sys

def MiddleMin(arr,start,middle,end):
    left=sys.maxsize
    right=sys.maxsize
    leftIndex=start
    rightIndex=start
    
    
    i=middle+1
    sum=0
    while (i<=end):
        
        #print (sum)
        #print (arr[i])
        sum+= arr[i]
        if(sum<right):
            right=sum
            rightIndex=i
        i+=1
        
        
    j=middle
    sum=0
    while(j>=start):
        
        #print (sum)
        #print (arr[j])
        sum+=arr[j]
        if(sum<left):
            left=sum
            leftIndex=j
        j-=1
    
    
    list = arr[leftIndex:rightIndex+1]
    
    return list

def min_subarray_finder_helper(arr,start,end):
    
    
    if(start >=end or len(arr)==1 or start==end):
        return [arr[start]]
    
    middle=(start+end)//2
    
    a =min_subarray_finder_helper(arr,start,middle)
    b= min_subarray_finder_helper(arr,middle+1,end)
    c= MiddleMin(arr,start,middle,end)
    
    
    #print(a,b,c)
    #print(c)
    if(sum(a)<sum(b)):
        
        if(sum(a)<sum(c)):
            return a
        else:
            return c
    else:
        if(sum(b)<sum(c)):
            return b
        else:
            return c
    
def min_subarray_finder(arr):
    return min_subarray_finder_helper(arr,0,len(arr)-1)
    
    
    
    
    
    
    


inpArr = [1, -4, -7, 5, -13, 9, 23, -1]
msa = min_subarray_finder(inpArr)
print(msa)
#Output: [-4, -7, 5, -13]
print(sum(msa))
#Output: -19
        
        

        
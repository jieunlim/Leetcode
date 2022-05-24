class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [int(x) for x in str(num)]
        sort_arr = sorted(arr, reverse=True)
        if arr==sort_arr: return num
        
        
        for i in range(len(arr)):
            if sort_arr[i] == arr[i]:
                continue
            else:
                
                temp = arr[i]
                arr[i] = sort_arr[i]
                find = sort_arr[i]

                
                for i in range(len(arr)-1, -1, -1):
                    if arr[i] == find: 
                        arr[i] = temp
                        break
                break
                
        sol = 0       
        for n in arr:
           
            sol = sol*10 + n


        return sol

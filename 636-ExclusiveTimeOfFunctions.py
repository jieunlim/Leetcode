class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        sol = [0] * n
        
        for log in logs:
            func, action, time = log.split(":")
            func, time = int(func), int(time)
      
            
            if action == "start":
                stack.append(time)
            else:
                start_time  = stack.pop()
                process_time  = time - start_time + 1
                sol[func] += process_time 
                
                for i in range(len(stack)):
                    stack[i] += process_time 
                    
        return sol

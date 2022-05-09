#O(n), O(n)

class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], '+'
        
        for i in range(len(s)):

            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s)-1:
                if sign in '+-':
                    stack.append(int(sign+str(num)))

                elif sign == '*':
                    prev = stack.pop()
                    stack.append(num * prev)

                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev/num))

                sign = s[i]
                num = 0

        return sum(stack)



class Solution2:
    def calculate(self, s: str) -> int:
        sol = 0
        stack = []
        
        def operation(sign, num):
            if sign=='+': stack.append(num)
            elif sign=='-': stack.append(-num)
            elif sign=='*': stack.append(stack.pop()*num)
            elif sign=='/': 
                prev = stack.pop()
                if prev < 0: 
                    stack.append(-(abs(prev)//num))
                else: 
                    stack.append(prev//num)
            
        cur, sign = 0, "+"
        
        for i in range(len(s)):

            if s[i].isdigit():
                cur = 10*cur + int(s[i])

            elif s[i] in '+-*/':
                operation(sign, cur)
                sign, cur = s[i], 0
                
        operation(sign, cur)


        return sum(stack)
        

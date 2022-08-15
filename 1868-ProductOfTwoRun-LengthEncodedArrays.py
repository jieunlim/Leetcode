class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        product = []
        
        e1 = e2 = 0
        
        while e1 < len(encoded1) and e2<len(encoded2):
            e1_val, e1_cnt = encoded1[e1] #[[1,0],[2,1],[3,2]]
            e2_val, e2_cnt = encoded2[e2] #[[2,0],[3,3]]
            
            product_val = e1_val * e2_val # 2
            product_cnt = min(e1_cnt, e2_cnt) #3
            
            
            encoded1[e1][1] -= product_cnt
            encoded2[e2][1] -= product_cnt
            
            if encoded1[e1][1] == 0:
                e1 += 1
            
            if encoded2[e2][1] == 0:
                e2 += 1
            
            if not product or product[-1][0] != product_val:
                    product.append([product_val, product_cnt])
            else: product[-1][1] += product_cnt
                
        return product
                    

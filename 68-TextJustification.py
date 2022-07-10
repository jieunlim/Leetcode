class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sol = []
        cur = []
        width = 0 # num of words in all cur
        
        for word in words:
        
            if len(word) + width + len(cur) <=maxWidth:
                cur.append(word)
                width += len(word)
                continue
            
            if len(cur) == 1:
                sol.append("{0:<{1}}".format(" ".join(cur), maxWidth))
                
            else:
                space = (maxWidth - width)// (len(cur)-1)
                extra = (maxWidth - width)% (len(cur)-1)
                
                i = 0
                
                while extra > 0:
                    cur[i] += " "
                    extra -=1
                    i += 1
                
                sol.append((" "*space).join(cur))
                
            cur = [word]
            width = len(word)
            
        sol.append("{0:<{1}}".format(" ".join(cur), maxWidth))
        
#       sol.append("{0: <{width}}".format(" ".join(cur), width=maxWidth))
        
        return sol

  
class Solution2:
	  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
	      sol = []
        width = 0		
        cur = []
        
        for word in words:
            #print(f"word:{word}, cur:{cur}, width = {width}, sol={sol}")
            #new word + cur length + space
            if (len(word) + width + len(cur)) <= maxWidth:
                width += len(word)
                cur.append(word)
                continue
            
            if len(cur) == 1:
                sol.append(' '.join(cur).ljust(maxWidth))
            else:
                space = (maxWidth - width)//(len(cur)-1)
                extra = (maxWidth - width)%(len(cur)-1)
			                  
                i = 0
				
                while extra > 0:
                    cur[i] += " "
                    extra -= 1
                    i += 1
                
                sol.append((" " * space).join(cur))
            
			#first word
            cur = [word]
            width = len(word)
            
		#left align with width
        sol.append(' '.join(cur).ljust(maxWidth))
        
        return sol

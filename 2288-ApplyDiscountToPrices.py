class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        rate = discount/100.00
        
        for i, word in enumerate(sentence):
            if word[0] == '$' and word[1:].isdigit():
                new_price = int(word[1:])*(1-rate)
                sentence[i] = '$' + '{:.2f}'.format(new_price)
        
        return " ".join(sentence)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort products 
        # ans, temp_ans = [], []
        # for i in range(len(searchWord)):
        #     for product in products:
        #         if product.startswith(searchWord[:i]):
        #             temp_ans.append(product)
        #     ans.append(temp_ans)
        # return ans
        
        # N = number of products, M = length of max product word, K = length of searchWord
        products.sort() # time O(MNlogN)
        ans, cur_ans, cur_word = [], [], []
        j = 0
        for i in range(len(searchWord)): # Kx
            cur_word.append(searchWord[i])
            while j < len(products) and len(cur_ans) < 3: # Nx
                cur_str = ''.join(cur_word)
                if products[j].startswith(cur_str):
                    cur_ans.append(products[j])
                elif products[j] > cur_str:
                    break
                j += 1
            j -= len(cur_ans)
            ans.append(cur_ans)
            cur_ans = []
        return ans
            
        
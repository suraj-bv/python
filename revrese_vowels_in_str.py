class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in 'aeiouAEIOU':
                vow.append(s[i])
        for i in range(len(s_list)):
            if s_list[i] in 'aeiouAEIOU':
                s_list[i] = vow[-1]
                vow.pop()
        
        return ''.join(s_list)
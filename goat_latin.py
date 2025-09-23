class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()

        for i,word in enumerate(words, start=1):
            if word[0] in "aeiouAEIOU":
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word = word + (i * "a")
            words[i - 1] = word

        return ' '.join(words)

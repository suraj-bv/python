class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keys = key.replace(" ", "")
        seen = []
        
        for ch in keys:
            if ch not in seen:
                seen.append(ch)

        a = "".join(seen)
        res = ''

        for char in message:
            if char == " ":
                res += char
            else:
                if char in a:
                    idx = a.index(char) + 97
                    res += chr(idx)

        return res

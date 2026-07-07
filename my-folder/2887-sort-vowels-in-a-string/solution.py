class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        v = []
        for i in s:
            if i in vowels:
                v.append(i)
        v.sort()
        res = list(s)
        v_id = 0
        for i in range(len(res)):
            if res[i] in vowels:
                res[i] = v[v_id]
                v_id += 1
        return "".join(res)

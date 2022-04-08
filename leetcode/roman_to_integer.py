class Solution:
    def romanToInt(self, s: str) -> int:
        romanValue = {
            'I': 1,
            'IV': 4,
            'IX': 9,
            'V': 5,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        sum = 0
        for i in range(len(s) - 1):
            if romanValue[s[i]] >= romanValue[s[i + 1]]:
                sum += romanValue[s[i]]
            else:
                sum -= romanValue[s[i]]

        sum += romanValue[s[len(s) - 1]]

        return sum
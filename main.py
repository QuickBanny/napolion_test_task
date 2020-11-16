
class Solution:

    def __init__(self):
        self.arab = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        self.roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    def roman_to_int(self, s: str) -> int:
        i = len(self.arab) - 1
        result = 0
        position = 0
        while i >= 0 and position < len(s):
            if s[position: position + len(self.roman[i])] == self.roman[i]:
                result += self.arab[i]
                position += len(self.roman[i])
            else:
                i -= 1

        return result


if __name__ == '__main__':
    pass
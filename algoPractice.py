## Integer to Roman - Leetcode 12 - Python
g = (1100 // 1100)
print(g, "hola")

class Solution:
  def convert(self, number: int) -> str:
    options = [["I", 1], ["V", 5], ["X", 10], ["IV", 4], ["IX", 9], ["XL", 40], ["L", 50] ,["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900] ,["M", 1000]]

    result = ""
    for symbol, value in reversed(options):
      if number // value:
        count  =  number // value
        result += (count * symbol)
        number = number % value
    return result

s = Solution()
gg = s.convert(1100)
print(gg)
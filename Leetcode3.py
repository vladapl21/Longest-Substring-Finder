class Solution(object):
  def lengthOfLongestSubstring(self, s):
      """
      :type s: str
      :rtype: int
      """
      stack = []
      max = 0
      for i in range(len(s)):
          if s[i] not in stack:
              stack.append(s[i])

          else:
              stack = stack[stack.index(s[i]) + 1:]
              stack.append(s[i])
          if len(stack) > max:
              max = len(stack)
          print(stack)
      return max
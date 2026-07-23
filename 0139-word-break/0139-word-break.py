class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(index):

            if index == len(s):
                return True

            if index in memo:
                return memo[index]

            for word in wordDict:

                if s.startswith(word, index):

                    if dfs(index + len(word)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False

        return dfs(0)
        
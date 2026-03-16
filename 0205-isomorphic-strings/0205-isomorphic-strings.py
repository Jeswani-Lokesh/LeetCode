class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}

        for a, b in zip(s, t):
            if a in map_s_to_t and map_s_to_t[a] != b:
                return False
            if b in map_t_to_s and map_t_to_s[b] != a:
                return False

            map_s_to_t[a] = b
            map_t_to_s[b] = a

        return True
        
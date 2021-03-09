class Solution:
    def defangIPaddr(self, address: str) -> str:
        out = ""
        for x in address:
            if x is '.':
                out += "[.]"
            else:
                out += x
        return out

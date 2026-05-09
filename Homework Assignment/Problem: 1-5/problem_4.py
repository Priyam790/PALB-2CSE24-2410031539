class Solution:
    def findUnion(self, a, b):

        # Python's set union operator does it all in one shot
        return list(set(a) | set(b))

        # Equivalent explicit version:
        # result = set()
        # for x in a: result.add(x)
        # for x in b: result.add(x)
        # return list(result)

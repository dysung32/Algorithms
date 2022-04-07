# 가장 무거운 두개의 돌 y, x (y>=x)
# x와 y가 같으면 두개 다 파괴
# x와 y가 다르면  x 파괴, y를 y - x로 바꾸기

class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort(reverse=True)
            stones.append(abs(stones[0] - stones[1]))
            stones.pop(0)
            stones.pop(0)
        return stones[0]
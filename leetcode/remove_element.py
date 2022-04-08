class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums: 정수 배열
        # val: 제거할 정수
        n = nums.count(val)
        for i in range(n):
            nums.remove(val)

        return len(nums)

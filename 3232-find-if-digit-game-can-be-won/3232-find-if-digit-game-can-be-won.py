class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        alice_sum=0
        bob_sum=0
        for i in range(len(nums)):
            if nums[i]<10:
                alice_sum+=nums[i]
            else:
                bob_sum+=nums[i]
        return alice_sum!=bob_sum
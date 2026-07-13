class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []

        for i in range(len(nums1)):
            ans = -1

           
            for k in range(len(nums2)):
                if nums2[k] == nums1[i]:

                    
                    for j in range(k + 1, len(nums2)):
                        if nums2[j] > nums2[k]:
                            ans = nums2[j]
                            break
                    break

            arr.append(ans)

        return arr
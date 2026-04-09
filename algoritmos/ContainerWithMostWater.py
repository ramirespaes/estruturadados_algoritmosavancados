class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maiorArea = 0

        while i < j:
            area_atual = (j - i) * min(height[i], height[j])
            maiorArea = max(maiorArea, area_atual)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maiorArea

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=left + 1
        max_profit=0

        while right < len(prices):
            if prices[right] < prices[left]:
                left=right

            else:
                profit=prices[right] - prices[left]
                max_profit=max(max_profit,profit)

            right+=1

        return max_profit

        
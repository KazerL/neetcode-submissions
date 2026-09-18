class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initial window
        left = 0 
        right = 1

        buy = prices[0]
        sell = 0

        buyIndex = 0
        sellIndex = 0

        profit = 0
        currDiff = 0
        profit = 0

        while right < len(prices):
            tempBuy = prices[left]
            tempSell = prices[right]

            if tempSell < tempBuy and right != len(prices) - 1:
                left = right
                right += 1
                currDiff = prices[right] - prices[left]

                if currDiff > profit:
                    maxDiff = currDiff
                    continue

                continue

            tempDiff = tempSell - tempBuy
            if tempDiff > profit:
                profit = tempDiff     

            right += 1

        return profit

        
        
def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest = 0
        for customer in accounts:
            sum = 0
            for bank in customer:
                sum += bank
            if sum > highest:
                highest = sum
        return highest

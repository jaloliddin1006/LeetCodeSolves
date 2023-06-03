class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        cassa = []
        for i in bills:
            if i == 5:
                cassa.append(i)
                continue
            if i == 10:
                if 5 in cassa:
                    cassa.remove(5)
                    cassa.append(10)
                    continue
                else:
                    return False
            if i == 20:
                if 5 in cassa and 10 in cassa :
                    cassa.remove(5)
                    cassa.remove(10)
                    cassa.append(20)
                    
                elif cassa.count(5) >= 3:
                    cassa.remove(5)
                    cassa.remove(5)
                    cassa.remove(5)
                    cassa.append(20)
                    continue
                    
                else:
                    return False
        return True
        

bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

print(Solution().lemonadeChange(bills))

# print(bills.remove(10))
# print(bills.count(5))

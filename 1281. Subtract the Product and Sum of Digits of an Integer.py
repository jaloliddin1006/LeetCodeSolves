class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d = {'mul':1, 'sum':0}
        for i in str(n):
            d['mul'] *= int(i)
            d['sum'] += int(i)
        return d['mul'] - d['sum']
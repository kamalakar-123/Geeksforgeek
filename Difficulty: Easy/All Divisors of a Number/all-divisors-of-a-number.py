class Solution:
    def getDivisors(self, n):
        divisors = []
    
        # Check numbers up to square root of n
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)         # Small factor
                if i != n // i:
                    divisors.append(n // i) # Pair factor
    
        divisors.sort()
        return divisors
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod=int(1e9)+7
        prime_count = 0

        for num in range(1, n + 1):
            fact_count = 0

            for i in range(1, num + 1):
                if num % i == 0:
                    fact_count += 1

            if fact_count == 2:
                prime_count += 1

        non_prime_count = n - prime_count

        prime_fact = 1
        for i in range(1, prime_count + 1):
            prime_fact *= i
        print(prime_fact)

        non_prime_fact = 1
        for i in range(1, non_prime_count + 1):
            non_prime_fact *= i

        return (prime_fact * non_prime_fact)%mod
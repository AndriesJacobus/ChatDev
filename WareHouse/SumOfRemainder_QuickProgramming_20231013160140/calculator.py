class Calculator:
    def calculate_sum_of_divisors(self, number):
        divisors = []
        for i in range(2, number):
            if number % i == 0:
                divisors.append(i)
        
        print(f"Divisors of {number} are {divisors}")
        return sum(divisors)
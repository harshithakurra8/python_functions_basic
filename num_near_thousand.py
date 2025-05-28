def near_thousand(n):
    return abs(1000 - n) <= 1000 or abs(2000 - n) <= 1000
test_numbers=[900,1100,1800,2100,5000]
for num in test_numbers:
    print(f"{num}is within 100 of 1000 or 2000: {near_thousand(num)}")
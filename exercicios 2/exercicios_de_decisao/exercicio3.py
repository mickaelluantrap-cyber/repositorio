pop_a = 80000
taxa_a = 3

pop_b = 200000
taxa_b = 1.5

anos = 0
while pop_a < pop_b:
    pop_a = pop_a * (1 + taxa_a / 100)
    pop_b = pop_b * (1 + taxa_b / 100)
anos += 1

print(f"demorarao {anos} anos")
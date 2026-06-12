def calculate_total_eggs():
    first_10_days = 10 * 2
    next_10_days = 10 * 3
    last_40_days = 40 * 6

    total_eggs = first_10_days + next_10_days + last_40_days
    return total_eggs


def calculate_zero_probability(total_eggs, actual_rate):
    zero_probability = (1 - actual_rate) ** total_eggs
    return zero_probability


base_rate = 0.001
parent_multiplier = 3
actual_rate = base_rate * parent_multiplier

total_eggs = calculate_total_eggs()
zero_probability = calculate_zero_probability(total_eggs, actual_rate)

print("Rock Kingdom Egg Probability Calculator")
print("---------------------------------------")
print("Days: 60")
print("Total eggs:", total_eggs)

print("Egg schedule:")
print("Days 1-10: 2 eggs per day")
print("Days 11-20: 3 eggs per day")
print("Days 21-60: 6 eggs per day")

print("Probability setting:")
print("Base rate: 0.10%")
print("Parent multiplier: 3x")
print("Actual rate per egg: 0.30%")

print("Result:")
print("Probability of getting zero special eggs:", round(zero_probability, 4))
print("That is about", round(zero_probability * 100, 2), "%")

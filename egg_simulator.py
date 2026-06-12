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

def monte_carlo_simulation(trials, total_eggs, actual_rate):
    zero_special_count = 0

    for trial in range(trials):
        special_eggs = simulate_one_attempt(total_eggs, actual_rate)

        if special_eggs == 0:
            zero_special_count += 1

    estimated_probability = zero_special_count / trials

    return estimated_probability


if __name__ == "__main__":
    # Settings
    days = 60
    base_rate = 0.001
    parent_multiplier = 3
    actual_rate = base_rate * parent_multiplier

    # Egg count
    total_eggs = calculate_total_eggs()

    # Exact probability
    exact_probability = calculate_exact_probability(total_eggs, actual_rate)

    # Monte Carlo simulation
    trials = 10000
    monte_carlo_probability = monte_carlo_simulation(
        trials,
        total_eggs,
        actual_rate
    )

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

print("Monte Carlo simulation:")
print(f"Number of simulations: {trials}")
print(f"Estimated probability of zero special eggs: {monte_carlo_probability:.4f}")
print(f"That is about {monte_carlo_probability * 100:.2f}%")

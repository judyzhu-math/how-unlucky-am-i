import random
import math


def calculate_total_eggs():
    """
    Calculate the total number of eggs based on the real egg schedule.

    Days 1-10: 2 eggs per day
    Days 11-20: 3 eggs per day
    Days 21-60: 6 eggs per day
    """

    eggs_first_10_days = 10 * 2
    eggs_next_10_days = 10 * 3
    eggs_last_40_days = 40 * 6

    total_eggs = eggs_first_10_days + eggs_next_10_days + eggs_last_40_days

    return total_eggs


def calculate_zero_probability(total_eggs, actual_rate):
    """
    Calculate the exact probability of getting zero special eggs.

    Formula:
    probability = (1 - actual_rate) ** total_eggs
    """

    zero_probability = (1 - actual_rate) ** total_eggs

    return zero_probability


def calculate_at_least_one_probability(total_eggs, actual_rate):
    """
    Calculate the probability of getting at least one special egg.

    Formula:
    probability = 1 - (1 - actual_rate) ** total_eggs
    """

    at_least_one_probability = 1 - (1 - actual_rate) ** total_eggs

    return at_least_one_probability


def eggs_needed_for_target_probability(target_probability, actual_rate):
    """
    Calculate how many eggs are needed to reach a target probability
    of getting at least one special egg.

    Formula:
    1 - (1 - actual_rate) ** n >= target_probability

    Rearranged:
    n >= log(1 - target_probability) / log(1 - actual_rate)
    """

    eggs_needed = math.log(1 - target_probability) / math.log(1 - actual_rate)

    return math.ceil(eggs_needed)


def simulate_one_attempt(total_eggs, actual_rate):
    """
    Simulate one player's egg breeding result.

    Return the number of special eggs after hatching total_eggs eggs.
    """

    special_eggs = 0

    for egg in range(total_eggs):
        if random.random() < actual_rate:
            special_eggs += 1

    return special_eggs


def monte_carlo_simulation(trials, total_eggs, actual_rate):
    """
    Run many simulations and estimate the probability of getting zero special eggs.

    trials means how many times we repeat the whole experiment.
    For example, trials = 10000 means simulating 10000 players.
    """

    zero_special_count = 0

    for trial in range(trials):
        special_eggs = simulate_one_attempt(total_eggs, actual_rate)

        if special_eggs == 0:
            zero_special_count += 1

    estimated_probability = zero_special_count / trials

    return estimated_probability


def print_case_result(case_name, base_rate, parent_multiplier, total_eggs, trials):
    """
    Print the probability results for one probability assumption.
    """

    actual_rate = base_rate * parent_multiplier

    zero_probability = calculate_zero_probability(total_eggs, actual_rate)
    at_least_one_probability = calculate_at_least_one_probability(
        total_eggs,
        actual_rate
    )

    monte_carlo_probability = monte_carlo_simulation(
        trials,
        total_eggs,
        actual_rate
    )

    print(case_name)
    print("-" * len(case_name))
    print(f"Base rate: {base_rate * 100:.2f}%")
    print(f"Parent multiplier: {parent_multiplier}x")
    print(f"Actual rate per egg: {actual_rate * 100:.2f}%")
    print()

    print("Exact mathematical result:")
    print(f"Probability of getting zero special eggs: {zero_probability:.6f}")
    print(f"That is about {zero_probability * 100:.4f}%")
    print(f"Probability of getting at least one special egg: {at_least_one_probability:.6f}")
    print(f"That is about {at_least_one_probability * 100:.4f}%")
    print()

    print("Monte Carlo simulation:")
    print(f"Number of simulations: {trials}")
    print(f"Estimated probability of zero special eggs: {monte_carlo_probability:.6f}")
    print(f"That is about {monte_carlo_probability * 100:.4f}%")
    print()

    print("Psychological pity table:")
    target_probabilities = [0.50, 0.80, 0.90, 0.95, 0.99]

    for target in target_probabilities:
        eggs_needed = eggs_needed_for_target_probability(target, actual_rate)
        print(f"{int(target * 100)}% chance of at least one special egg: {eggs_needed} eggs")

    print()
    print("=" * 60)
    print()


if __name__ == "__main__":
    # Egg settings
    days = 60
    total_eggs = calculate_total_eggs()

    # Game mechanism assumption
    parent_multiplier = 3

    # Monte Carlo setting
    trials = 10000

    print("Rock Kingdom Egg Probability Calculator")
    print("---------------------------------------")
    print(f"Days: {days}")
    print(f"Total eggs: {total_eggs}")
    print()

    print("Egg schedule:")
    print("Days 1-10: 2 eggs per day")
    print("Days 11-20: 3 eggs per day")
    print("Days 21-60: 6 eggs per day")
    print()

    print("Note:")
    print("The exact base rate is unknown.")
    print("The source only says that the normal rate is below 1%.")
    print("So this program compares two assumptions.")
    print()
    print("=" * 60)
    print()

    print_case_result(
        case_name="Case 1: Conservative assumption",
        base_rate=0.001,
        parent_multiplier=parent_multiplier,
        total_eggs=total_eggs,
        trials=trials
    )

    print_case_result(
        case_name="Case 2: High-rate assumption",
        base_rate=0.0099,
        parent_multiplier=parent_multiplier,
        total_eggs=total_eggs,
        trials=trials
    )

import random
import math
import os
import matplotlib.pyplot as plt



def calculate_total_eggs():
    """
    Calculate the total number of eggs based on the real egg schedule.

    Days 1-10: 2 eggs per day
    Days 11-20: 3 eggs per day
    Days 21-60: 5 eggs per day
    """
    eggs_first_10_days = 10 * 2
    eggs_next_10_days = 10 * 3
    eggs_last_40_days = 40 * 5

    total_eggs = eggs_first_10_days + eggs_next_10_days + eggs_last_40_days

    return total_eggs


def calculate_zero_probability(total_eggs, actual_rate):
    """
    Calculate the exact probability of getting zero special eggs.
    """
    zero_probability = (1 - actual_rate) ** total_eggs
    return zero_probability


def calculate_at_least_one_probability(total_eggs, actual_rate):
    """
    Calculate the probability of getting at least one special egg.
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


def monte_carlo_results(trials, total_eggs, actual_rate):
    """
    Run many simulations and return all simulation results.

    Each result is the number of special eggs obtained by one simulated player.
    """
    results = []

    for trial in range(trials):
        special_eggs = simulate_one_attempt(total_eggs, actual_rate)
        results.append(special_eggs)

    return results


def estimate_zero_probability_from_results(results):
    """
    Estimate the probability of getting zero special eggs from simulation results.
    """
    zero_special_count = 0

    for result in results:
        if result == 0:
            zero_special_count += 1

    estimated_probability = zero_special_count / len(results)

    return estimated_probability


def calculate_probabilities(base_rate, parent_multiplier, total_eggs):
    """
    Calculate theoretical probabilities for special egg results.

    Returns:
        probability_no_special: probability of getting zero special eggs
        probability_at_least_one: probability of getting at least one special egg
    """
    actual_rate = base_rate * parent_multiplier

    probability_no_special = calculate_zero_probability(total_eggs, actual_rate)
    probability_at_least_one = calculate_at_least_one_probability(total_eggs, actual_rate)

    return probability_no_special, probability_at_least_one


def count_distribution(results):
    """
    Count how many simulated players got 0, 1, 2, 3, ... special eggs.
    """
    distribution = {}

    for result in results:
        if result not in distribution:
            distribution[result] = 0

        distribution[result] += 1

    return distribution


def plot_probability_comparison(total_eggs, parent_multiplier):
    """
    Plot probability comparison between two rate assumptions.
    """
    case_names = [
        "Conservative\n0.1%",
        "High-rate\n0.99%"
    ]

    base_rates = [0.001, 0.0099]

    no_special_probabilities = []
    at_least_one_probabilities = []

    for base_rate in base_rates:
        probability_no_special, probability_at_least_one = calculate_probabilities(
            base_rate=base_rate,
            parent_multiplier=parent_multiplier,
            total_eggs=total_eggs
        )

        no_special_probabilities.append(probability_no_special * 100)
        at_least_one_probabilities.append(probability_at_least_one * 100)

    x_positions = range(len(case_names))

    plt.figure(figsize=(8, 5))

    plt.bar(
        [x - 0.2 for x in x_positions],
        no_special_probabilities,
        width=0.4,
        label="Zero special eggs"
    )

    plt.bar(
        [x + 0.2 for x in x_positions],
        at_least_one_probabilities,
        width=0.4,
        label="At least one special egg"
    )

    plt.xticks(list(x_positions), case_names)
    plt.ylabel("Probability (%)")
    plt.title("Special Egg Probability Comparison")
    plt.legend()
    plt.tight_layout()

    os.plt.savefig("images/probability_comparison.png")
    plt.show()


def plot_monte_carlo_distribution(results, case_name):
    """
    Plot the distribution of special eggs from Monte Carlo simulation.
    """
    distribution = count_distribution(results)

    special_egg_numbers = sorted(distribution.keys())
    player_counts = []

    for number in special_egg_numbers:
        player_counts.append(distribution[number])

    plt.figure(figsize=(8, 5))

    plt.bar(special_egg_numbers, player_counts)

    plt.xlabel("Number of special eggs obtained")
    plt.ylabel("Number of simulated players")
    plt.title(f"Monte Carlo Distribution: {case_name}")
    plt.xticks(special_egg_numbers)
    plt.tight_layout()

    os.plt.savefig("images/monte_carlo_distribution.png")
    plt.show()


def print_case_result(case_name, base_rate, parent_multiplier, total_eggs, trials):
    """
    Print the probability results for one probability assumption.

    Returns:
        results: Monte Carlo simulation results for this case
    """
    actual_rate = base_rate * parent_multiplier

    zero_probability = calculate_zero_probability(total_eggs, actual_rate)
    at_least_one_probability = calculate_at_least_one_probability(
        total_eggs,
        actual_rate
    )

    results = monte_carlo_results(
        trials,
        total_eggs,
        actual_rate
    )

    monte_carlo_probability = estimate_zero_probability_from_results(results)

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
    print(f"Average number of special eggs: {sum(results) / len(results):.4f}")
    print(f"Maximum number of special eggs in one simulation: {max(results)}")
    print()

    print("Psychological pity table:")
    target_probabilities = [0.50, 0.80, 0.90, 0.95, 0.99]

    for target in target_probabilities:
        eggs_needed = eggs_needed_for_target_probability(target, actual_rate)
        print(f"{int(target * 100)}% chance of at least one special egg: {eggs_needed} eggs")

    print()
    print("=" * 60)
    print()

    return results


if __name__ == "__main__":
    # Egg settings
    days = 60
    total_eggs = calculate_total_eggs()

    # Game mechanism assumption
    parent_multiplier = 3

    # Monte Carlo setting
    trials = 10000

    print("Roco Kingdom Egg Probability Calculator")
    print("---------------------------------------")
    print(f"Days: {days}")
    print(f"Total eggs: {total_eggs}")
    print()

    print("Egg schedule:")
    print("Days 1-10: 2 eggs per day")
    print("Days 11-20: 3 eggs per day")
    print("Days 21-60: 5 eggs per day")
    print()

    print("Note:")
    print("The exact base rate is unknown.")
    print("The source only says that the normal rate is below 1%.")
    print("So this program compares two assumptions.")
    print()
    print("=" * 60)
    print()

    conservative_results = print_case_result(
        case_name="Case 1: Conservative assumption",
        base_rate=0.001,
        parent_multiplier=parent_multiplier,
        total_eggs=total_eggs,
        trials=trials
    )

    high_rate_results = print_case_result(
        case_name="Case 2: High-rate assumption",
        base_rate=0.0099,
        parent_multiplier=parent_multiplier,
        total_eggs=total_eggs,
        trials=trials
    )

    plot_probability_comparison(
        total_eggs=total_eggs,
        parent_multiplier=parent_multiplier
    )

    plot_monte_carlo_distribution(
        results=conservative_results,
        case_name="Conservative assumption"
    )

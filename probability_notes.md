# Probability Notes

This project analyzes the probability of getting a shiny or rare-colored egg in Rock Kingdom.

## Background

The exact base probability of getting a shiny / rare-colored egg is unknown.

The source only says that the normal rate is below 1%.

Because of this uncertainty, this project compares two assumptions:

- Conservative assumption: base rate = 0.1%
- High-rate assumption: base rate = 0.99%

Since all of my male breeding pets are rare-colored, I use a parent multiplier of 3.

## Egg Schedule

My egg production was not the same every day.

```text
Days 1-10: 2 eggs per day
Days 11-20: 3 eggs per day
Days 21-60: 5 eggs per day
```

So the total number of eggs is:

```text
10 × 2 + 10 × 3 + 40 × 5
= 20 + 30 + 200
= 250 eggs
```

## Formula

For each egg, the probability of getting a special egg is called the actual rate.

The probability of getting zero special eggs after many eggs is:

```text
Probability of zero special eggs = (1 - actual_rate)^total_eggs
```

The probability of getting at least one special egg is:

```text
Probability of at least one special egg = 1 - (1 - actual_rate)^total_eggs
```

## Case 1: Conservative Assumption

In this case, the base rate is assumed to be 0.1%.

```text
Base rate = 0.1% = 0.001
Parent multiplier = 3
Actual rate = 0.001 × 3 = 0.003 = 0.3%
```

So each egg has a 0.3% chance of becoming shiny or rare-colored.

For 250 eggs:

```text
Probability of zero special eggs = (1 - 0.003)^250
= 0.997^250
≈ 0.4718
```

That is about:

```text
47.18%
```

The probability of getting at least one special egg is:

```text
1 - 0.4718 = 0.5282
```

That is about:

```text
52.82%
```

### Interpretation

Under the conservative assumption, getting zero shiny / rare-colored eggs after 250 eggs is unlucky, but still very possible.

## Case 2: High-Rate Assumption

In this case, the base rate is assumed to be 0.99%.

```text
Base rate = 0.99% = 0.0099
Parent multiplier = 3
Actual rate = 0.0099 × 3 = 0.0297 = 2.97%
```

So each egg has a 2.97% chance of becoming shiny or rare-colored.

For 250 eggs:

```text
Probability of zero special eggs = (1 - 0.0297)^250
= 0.9703^250
≈ 0.000533
```

That is about:

```text
0.0533%
```

The probability of getting at least one special egg is:

```text
1 - 0.000533 = 0.999467
```

That is about:

```text
99.9467%
```

### Interpretation

Under the high-rate assumption, getting zero shiny / rare-colored eggs after 250 eggs is extremely unlucky.

If the real base rate is close to 1%, then my result is very rare.

## Monte Carlo Simulation

Besides exact mathematical calculation, this project also uses Monte Carlo simulation.

Monte Carlo simulation means repeating the same random experiment many times.

In this project, one simulation represents one player hatching 250 eggs.

For example, if the program runs 10,000 simulations, it is like simulating 10,000 players who each hatch 250 eggs.

For each simulated player, the program checks whether they get zero shiny / rare-colored eggs.

Then it estimates the probability by calculating:

```text
number of simulations with zero special eggs / total number of simulations
```

The Monte Carlo result should be close to the exact probability, but it may be slightly different each time because it uses randomness.

## Psychological Pity Table

There is no real guaranteed pity unless the game has a built-in pity system.

These numbers only show how many eggs are needed to reach each probability level mathematically.

### Conservative Assumption: Actual Rate = 0.3%

```text
50% chance of at least one special egg: 231 eggs
80% chance of at least one special egg: 536 eggs
90% chance of at least one special egg: 767 eggs
95% chance of at least one special egg: 998 eggs
99% chance of at least one special egg: 1533 eggs
```

Under this assumption, 250 eggs is only slightly above the 50% line.

### High-Rate Assumption: Actual Rate = 2.97%

```text
50% chance of at least one special egg: 23 eggs
80% chance of at least one special egg: 54 eggs
90% chance of at least one special egg: 77 eggs
95% chance of at least one special egg: 100 eggs
99% chance of at least one special egg: 153 eggs
```

Under this assumption, 250 eggs is already far beyond the 99% psychological pity line.

## Conclusion

The result depends strongly on the assumed base probability.

If the base rate is 0.1%, then getting zero special eggs after 250 eggs has a probability of about 47.18%. This is unlucky, but still very possible.

If the base rate is 0.99%, then getting zero special eggs after 250 eggs has a probability of about 0.0533%. This is extremely rare.

In short:

```text
Conservative assumption: unlucky, but possible.
High-rate assumption: extremely unlucky.
```

The egg gods are cruel, and probability is now part of the investigation.

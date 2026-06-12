# Probability Notes

This project analyzes the probability of getting a shiny or rare-colored egg in Rock Kingdom.

## Assumptions

The base probability of getting a shiny / rare-colored egg is assumed to be:

0.1% = 0.001

Since all of my male breeding pets are rare-colored, I use a parent multiplier of 3.

Therefore, the actual probability per egg is:

0.001 × 3 = 0.003

So each egg has a 0.3% chance of becoming a shiny / rare-colored egg.

## Egg Schedule

My egg production was not the same every day.

- Days 1-10: 2 eggs per day
- Days 11-20: 3 eggs per day
- Days 21-60: 6 eggs per day

So the total number of eggs is:

10 × 2 + 10 × 3 + 40 × 6

= 20 + 30 + 240

= 290 eggs

## Probability of Getting Zero Special Eggs

If the probability of getting a special egg is 0.3%, then the probability of not getting one is:

1 - 0.003 = 0.997

The probability of getting zero special eggs after 290 eggs is:

0.997^290 ≈ 0.4184

That is about:

41.84%

## Monte Carlo Simulation

Besides the exact formula, this project also uses a Monte Carlo simulation.

Monte Carlo simulation means repeating the same random experiment many times. In this project, one simulation represents one player hatching 290 eggs.

For example, if the program runs 10,000 simulations, it is like simulating 10,000 players who each hatch 290 eggs. (10,000 me in the parallel time and space)

For each simulated player, the program counts whether they get zero special eggs. Then it estimates the probability by calculating:

number of simulations with zero special eggs / total number of simulations

The Monte Carlo result should be close to the exact probability, but it may be slightly different each time because it uses randomness.

## Conclusion

With a 0.3% chance per egg, getting zero shiny / rare-colored eggs after 290 eggs is unlucky, but still very possible.

In other words, I am suffering especially all of my friends who play this game already had at least one special egg, but the math says this suffering is statistically allowed.

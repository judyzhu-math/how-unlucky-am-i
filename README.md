# how-unlucky-am-i
A Monte Carlo simulation project for estimating rare shiny egg probabilities using Python.
# Shiny Egg Probability Simulator

This project uses Monte Carlo simulation to estimate the probability of getting at least one rare shiny egg in a game named Rocokingdom.

## Background
In Rock Kingdom, players can place pet nests in their home. When two pets of the same species are placed together, they may produce an egg. These eggs have a small chance of becoming a shiny egg, an alternate-color egg, or even a shiny alternate-color egg.

I placed ten pet nests in my home(which is the maximum each player could place in their home) and played for about two months, but I still did not get a single shiny or alternate-color egg. Out of frustration and curiosity, I decided to use probability and Python simulation to answer the question:

How unlucky am I, mathematically?

According to the breeding mechanism I use in this project:

The base probability of getting a shiny / rare-colored egg is assumed to be 0.1%.
Since all of my male breeding pets are rare-colored, I use a parent multiplier of 3.
Therefore, the actual probability per egg is:
0.1% × 3 = 0.3%

So each egg has a 0.3% chance of becoming shiny or rare-colored.

## Egg schedule
My egg production was not the same every day.

Days 1-10: 2 eggs per day
Days 11-20: 3 eggs per day
Days 21-60: 6 eggs per day

The total number of eggs is:

10 × 2 + 10 × 3 + 40 × 6 = 290 eggs

## What this project does
This project calculates the probability of getting zero shiny / rare-colored eggs after 290 eggs.

It uses two methods:

Exact mathematical calculation
Monte Carlo simulation

The exact formula is:

(1 - 0.003)^290

The Monte Carlo simulation repeats the egg-breeding experiment many times. For example, it can simulate 10,000 players, where each player hatches 290 eggs. Then it estimates how often a player gets zero shiny / rare-colored eggs.

## Results
With an actual probability of 0.3% per egg, the probability of getting zero shiny / rare-colored eggs after 290 eggs is about:

41.84%

This means my result is unlucky, but still statistically possible.

In other words, I am suffering, but the math says this suffering is allowed.

## My egg nests
Here are my egg nests in Roco Kingdom:
![My egg nests](images/egg_nests.png)

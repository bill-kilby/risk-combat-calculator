# Risk Combat Calculator
A Monte Carlo simulator of the [Risk board game](https://en.wikipedia.org/wiki/Risk_(game)) (using LOTR rules). 

## Project Overview

This project allows for the probabilities to be generated for every possible individual combat situation in Risk.

The `main.py` script will run everything required, taking in the amount of permutations (explained further in Getting Started).
This will then output the simulation results, based on the amount of permutations, to both the console and a `csv` file containing all the parameters for each test, and result.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a816f6f-f8d3-452e-84f9-5e2fd1ecc58d" alt="drawing" width="50%"/>
</p>

<p align="center"><i>Example console output after running 1,000,000 iterations per test case.</i></p>


## Getting Started

### Dependencies

* Python 3.11.3
* Colorama 0.4.6

### Installing

**For running the script:**
* Clone the whole repository, or just the `/scripts/` folder, if you are only interested in running scripts.
* *If you want to skip installation, I have provided many outputs of iterations, ranging from 1 iteration to 1,000,000 iterations (per test case), in the "example_outputs" folder.*

**If you are interested in the documentation:**
* Sphinx documentation can be found under the `/docs/` folder, or [on my website.](https://billkilby.dev/docs/risk_combat_calculator/index.html)

### Executing program

#### Running the script

* Navigate to the `/scripts/` folder in your chosen console.
* Then, run the script by executing the following line, where ITERATIONS is the number of iterations per test case (1 for 1 iteration, 15 for 15 iterations, etc).
```
python main.py ITERATIONS
```

#### Adding/Removing Test Cases
Within the `/scripts` folder, there is a `test_cases.py` file. This contains all of the test cases that will be ran. The program will use this and automatically generate the output for it.
- *I made this purposefully verbose - every possible test case is in here.*

The parameters for the `test_cases` mean the following:
- attackers: The amount of attackers.
- defenders: The amount of defenders.
- attacker_has_leade: Whether or not the attacker has a leader (+1 to top dice if so).
- defender_has_leader: Whether or not the defender has a leader (+1 to top dice if so).
- has_stronghold: Whether or not there is a stronghold in the defender's tile (+1 to top dice if so).

#### Explanation of Output
The results of the tests will be printed to the console, and saved to a CSV. The parameters for the results mean the following:
- AKils: The amount of kills the attacker scored on average.
- AWins: The chance of attacker winning the test case.
- DKils: The amount of kills the defender scored on average.
- DWins: The chance of defender winning the test case.
- Time Taken: The amount of time taken for all iterations for that specific test case.

*Where "average" means the mean of all test case iterations, and "win" means:*
- For attacker; Destroying all Defender batallions (winning the territory).
- For defender; Not getting all batallions destroyed (keeping the territory).

## License

This project is licensed under the [Apache 2.0] License - see the LICENSE.md file for details

# Risk Combat Calculator
A Monte Carlo simulator of the [Risk board game](https://en.wikipedia.org/wiki/Risk_(game)) (using LOTR rules). 

## Project Overview

This project allows for the probabilities to be generated for every possible individual combat situation in Risk.

The `main.py` script will run everything required, taking in the amount of permutations (explained further in Getting Started).
This will then output the simulation results, based on the amount of permutations, to both the console and a `csv` file containing all the parameters for each test, and result.

## Getting Started

### Dependencies

* Python 3.11.3
TBD - colorama, etc.

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
Basically direct to test_cases.py and tell them to add remove here. note that all possible scenarios are here.


#### Explanation of Output
What each output means
Also, what "win" means.

## License

This project is licensed under the [Apache 2.0] License - see the LICENSE.md file for details

# BisectionRootFinder

**BisectionRootFinder** is a Python program that calculates the root of a given function \( f(x) \) within a specified interval \([a, b]\) using the Bisection Method. The program accepts an error tolerance \( e \) to determine the desired precision for the root approximation. Additionally, it calculates and reports the order of convergence for the iterative method based on the reduction in error across iterations.

## Features
- Finds the approximate root of a function within a specified interval.
- Uses the Bisection Method, a reliable root-finding technique for continuous functions.
- Calculates the order of convergence based on iterative errors.
- Provides error checking to ensure a valid interval for root-finding.

## Requirements
- Python 3.x
- Basic knowledge of lambda functions for inputting the target function.

## Usage

### Input
The program requires:
1. A lambda function representing \( f(x) \).
2. The interval bounds \( a \) and \( b \), with \( f(a) \) and \( f(b) \) having opposite signs.
3. The desired error tolerance \( e \) for root precision.

### Example Input
```plaintext
Enter your function as a lambda expression (e.g., lambda x: x**2 - 4): lambda x: x**3 - x - 2
Enter the lower bound of the interval a: 1
Enter the upper bound of the interval b: 2
Enter the error tolerance e: 0.0001
```

### Example Output
```plaintext
Approximate root: 1.521393
Number of iterations: 14
Order of convergence: 1.000000
```

## Notes
- Ensure that the chosen interval \([a, b]\) includes a sign change for \( f(a) \) and \( f(b) \) to guarantee the presence of a root.
- The convergence order should ideally be close to 1 for the Bisection Method, confirming linear convergence.

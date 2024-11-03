import math

# Function for Bisection Method
def bisection_method(f, a, b, e):
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    c = a
    iterations = 0
    errors = []

    while (b - a) / 2.0 > e:
        c = (a + b) / 2.0
        errors.append(abs(b - a) / 2.0)
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

    # Print the approximate root
    print(f"Approximate root: {c:.6f}")
    print(f"Number of iterations: {iterations}")

    # Calculate and print the order of convergence
    if len(errors) >= 3:
        convergence_order = math.log(errors[-1] / errors[-2]) / math.log(errors[-2] / errors[-3])
        print(f"Order of convergence: {convergence_order:.6f}")
    else:
        print("Insufficient data to calculate the order of convergence.")

# Get user input
def main():
    # Define the function
    f_input = input("Enter your function as a lambda expression (e.g., lambda x: x**2 - 4): ")
    f = eval(f_input)

    # Get the interval
    a = float(input("Enter the lower bound of the interval a: "))
    b = float(input("Enter the upper bound of the interval b: "))

    # Get the error tolerance
    e = float(input("Enter the error tolerance e: "))

    # Execute the bisection method
    bisection_method(f, a, b, e)

if __name__ == "__main__":
    main()

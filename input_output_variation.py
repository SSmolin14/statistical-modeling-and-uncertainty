import numpy as np

def main():
    print("Statistical Uncertainty Modeling: Area Calculation\n")
    # Get user input for mean and standard deviation
    try:
        mean_length = float(input("Enter the mean length of the side: "))
        stddev_length = float(input("Enter the standard deviation of the side: "))
    except ValueError:
        print("Please enter valid numbers for mean and standard deviation.")
        return

    num_samples = 1000

    # Generate random lengths based on normal distribution
    lengths = np.random.normal(loc=mean_length, scale=stddev_length, size=num_samples)

    # Calculate areas by squaring lengths
    areas = lengths ** 2

    # Compute statistics for area
    mean_area = np.mean(areas)
    stddev_area = np.std(areas)

    # Display results
    print(f"\nResults based on {num_samples} samples:")
    print(f"Mean area: {mean_area:.4f}")
    print(f"Standard deviation of area: {stddev_area:.4f}")

if __name__ == "__main__":
    main()

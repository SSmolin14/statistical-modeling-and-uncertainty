import numpy as np

def main():
    print("Statistical Uncertainty Modeling: 1D Calculation\n")
    # Get user input for mean and standard deviation
    try:
        mean_lengthA = float(input("Enter the mean length of the side A: "))
        mean_lengthB = float(input("Enter the mean length of the side B: "))
        stddev_lengthA = float(input("Enter the standard deviation of the side A: "))
        stddev_lengthB = float(input("Enter the standard deviation of the side B: "))
    except ValueError:
        print("Please enter valid numbers for mean and standard deviation.")
        return

    num_samples = 1000

    # Generate random lengths based on normal distribution
    lengths1 = np.random.normal(loc=mean_lengthA, scale=stddev_lengthA, size=num_samples)
    lengths2 = np.random.normal(loc=mean_lengthB, scale=stddev_lengthB, size=num_samples)

    # Calculate areas by squaring lengths
    areas = lengths1 * lengths2

    # Compute statistics for area
    mean_area = np.mean(areas)
    stddev_area = np.std(areas)

    # Display results
    print(f"\nResults based on {num_samples} samples:")
    print(f"Mean area: {mean_area:.4f}")
    print(f"Standard deviation of area: {stddev_area:.4f}")

if __name__ == "__main__":
    main()

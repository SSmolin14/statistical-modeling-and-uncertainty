import argparse
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# ...existing code...
def parse_args():
    p = argparse.ArgumentParser(description="Generate length samples and plot distributions.")
    p.add_argument("--meanA", type=float, help="Mean length of side A")
    p.add_argument("--meanB", type=float, help="Mean length of side B")
    p.add_argument("--stdA", type=float, help="Standard deviation of side A")
    p.add_argument("--stdB", type=float, help="Standard deviation of side B")
    p.add_argument("--samples", type=int, default=1000, help="Number of samples (default: 1000)")
    p.add_argument("--seed", type=int, help="Random seed for reproducibility")
    p.add_argument("--out", type=str, default="distributions.png", help="Output image filename")
    p.add_argument("--show", action="store_true", help="Show the figure interactively (may require a display)")
    return p.parse_args()

def collect_parameters(args):
    try:
        meanA = args.meanA if args.meanA is not None else float(input("Enter the mean length of the side A: "))
        meanB = args.meanB if args.meanB is not None else float(input("Enter the mean length of the side B: "))
        stdA = args.stdA if args.stdA is not None else float(input("Enter the standard deviation of the side A: "))
        stdB = args.stdB if args.stdB is not None else float(input("Enter the standard deviation of the side B: "))
    except ValueError:
        print("Please enter valid numbers for mean and standard deviation.")
        sys.exit(1)
    if stdA < 0 or stdB < 0:
        print("Standard deviations must be non-negative.", file=sys.stderr)
        sys.exit(1)
    if args.samples <= 0:
        print("Number of samples must be positive.", file=sys.stderr)
        sys.exit(1)
    return meanA, meanB, stdA, stdB

def compute_samples(meanA, meanB, stdA, stdB, samples, seed):
    rng = np.random.default_rng(seed)
    lengths1 = rng.normal(loc=meanA, scale=stdA, size=samples)
    lengths2 = rng.normal(loc=meanB, scale=stdB, size=samples)
    areas = lengths1 * lengths2
    return lengths1, lengths2, areas

def print_stats(arr, name):
    print(f"{name}: mean={np.mean(arr):.4f}, std={np.std(arr):.4f}, median={np.median(arr):.4f}")

def plot_and_save(lengths1, lengths2, areas, out_path, show=False):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))
    bins = 40

    axes[0].hist(lengths1, bins=bins, density=True, color="#4C72B0", alpha=0.8)
    axes[0].set_title("Distribution of lengths1 (side A)")
    axes[0].set_xlabel("Length")
    axes[0].set_ylabel("Density")
    axes[0].grid(True, alpha=0.3)

    axes[1].hist(lengths2, bins=bins, density=True, color="#55A868", alpha=0.8)
    axes[1].set_title("Distribution of lengths2 (side B)")
    axes[1].set_xlabel("Length")
    axes[1].grid(True, alpha=0.3)

    axes[2].hist(areas, bins=bins, density=True, color="#C44E52", alpha=0.8)
    axes[2].set_title("Distribution of areas (A * B)")
    axes[2].set_xlabel("Area")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle("Sample Distributions", fontsize=14)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    out_abs = os.path.abspath(out_path)
    fig.savefig(out_abs, dpi=150)
    print(f"Saved distribution figure to: {out_abs}")

    if show:
        try:
            plt.show()
        except Exception as e:
            print(f"Could not show figure interactively: {e}", file=sys.stderr)

def main():
    print("Statistical Uncertainty Modeling: 1D Calculation\n")
    args = parse_args()
    meanA, meanB, stdA, stdB = collect_parameters(args)
    lengths1, lengths2, areas = compute_samples(meanA, meanB, stdA, stdB, args.samples, args.seed)

    print(f"\nResults based on {args.samples} samples:")
    print_stats(lengths1, "lengths1")
    print_stats(lengths2, "lengths2")
    print_stats(areas, "areas")

    plot_and_save(lengths1, lengths2, areas, args.out, show=args.show)

if __name__ == "__main__":
    main()
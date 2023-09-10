# Start a new AOC day. Set up a directory called day_x under the solutions
# directory, create a new python file called solution.py, and make use of
# aocd to download the input for the day and the sample input, and
# the problem description.

import os
import sys
import aocd

def main():
    # Check that the AOC_SESSION environment variable is set
    if os.environ.get("AOC_SESSION") is None:
        print("AOC_SESSION environment variable not set")
        # Ask the user for the session token
        token = input("Enter your session token: ")
        os.environ["AOC_SESSION"] = token

    # Get the day number from the command line
    if len(sys.argv) != 2:
        print("Usage: start_day.py <day_number>")
        sys.exit(1)
    day = sys.argv[1]

    # Create the directory for the day
    day_dir = os.path.join("solutions", "day_" + day)
    if os.path.exists(day_dir):
        print("Day directory already exists, using existing directory")
    os.mkdir(day_dir)

    # Create the python file for the day
    solution_file = os.path.join(day_dir, "solution.py")
    if os.path.exists(solution_file):
        print("Solution file already exists, using existing file")
    else:
        print("Creating solution file")
        with open(solution_file, "w") as f:

            # Write the header
            f.write("# Path: solutions/day_" + day + "/solution.py\n")
            f.write("# -----")
            f.write("#\n")
            f.write("# Solution for day " + day + " of the Advent of Code 2017 challenge\n")
            f.write("# https://adventofcode.com/2017/day/" + day + "\n")
            f.write("#\n")
            f.write("# Freyr Helgason\n")
            f.write("# github.com/freyrh/AdventOfCode2017\n")
            f.write("#\n")
            f.write("# -----")
            f.write("\n\n")

    # Set today's access token
    aocd.set_cookie(os.environ.get("AOC_SESSION"))

    # Download the input and save it to a file in the day directory
    input_file = os.path.join(day_dir, "input.txt")
    if os.path.exists(input_file):
        print("Input data file already exists, skipping")
    else:
        print("Downloading input data to input.txt")
        input_data = aocd.get_data(day=int(day))
        with open(input_file, "w") as f:
            f.write(input_data)

    # Download the sample input and save it to a file in the day directory
    sample_file = os.path.join(day_dir, "input_ex.txt")
    if os.path.exists(sample_file):
        print("Sample data file already exists, skipping")
    else:
        print("Downloading sample input data to input_ex.txt")
        sample_data = aocd.get_data(day=int(day), block=1)
        with open(sample_file, "w") as f:
            f.write(sample_data)

    # Download the problem description and save it to a file in the day directory
    desc_file = os.path.join(day_dir, "description.txt")
    if os.path.exists(desc_file):
        print("Description file already exists, skipping")
    else:
        print("Downloading problem description to description.txt")
        desc_data = aocd.get_data(day=int(day), block=0)
        with open(desc_file, "w") as f:
            f.write(desc_data)

    # Open the solution, input example and description files in the default editor
    os.system("code " + solution_file)
    os.system("code " + sample_file)
    os.system("code " + desc_file)

if __name__ == "__main__":
    main()



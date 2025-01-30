import json
from utils import compute_scores

def main():
    """
    Main function to process persons.json, compute coworker scores, and print results.
    """
    input_file = "persons.json"
    try:
        # Load input data
        with open(input_file, "r") as file:
            persons = json.load(file)

        # Compute coworker scores
        results = compute_scores(persons)

        # Handle cases where no results are found
        if not results:
            print("No coworker pairs found.")
            return

        # Extract the top 10% of results
        top_10_percent = results[:max(1, len(results) // 10)]

        # Print results
        for record in top_10_percent:
            print(f"{record[0]}, {record[1]}, {record[2]}, {record[3]:.2f}{record[4]}")
        print(f"\n{len(top_10_percent)} records printed.")

    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please ensure the file exists in the current directory.")
    except json.JSONDecodeError:
        print(f"Error: {input_file} is not a valid JSON file. Please check the file format.")

if __name__ == "__main__":
    main()

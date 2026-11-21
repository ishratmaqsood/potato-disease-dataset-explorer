import csv
import os

DATA_FILE = "sample_data.csv"


def load_data():
    """Load potato leaf sample records from the CSV file."""
    try:
        with open(DATA_FILE, newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Could not find {DATA_FILE}. Keep it in the same folder as main.py.")
        return []


def show_summary(records):
    if not records:
        print("No records found.")
        return

    counts = {}
    for record in records:
        disease = record["disease"].strip()
        counts[disease] = counts.get(disease, 0) + 1

    print("\n--- Potato Leaf Dataset Summary ---")
    print(f"Total samples: {len(records)}")
    for disease, count in sorted(counts.items()):
        print(f"{disease}: {count}")


def search_disease(records):
    query = input("Enter a disease name to search: ").strip().lower()
    matches = [
        row for row in records
        if query in row["disease"].lower()
    ]

    if matches:
        print("\nMatching samples:")
        for row in matches:
            print(f"- {row['image_name']} ({row['disease']})")
    else:
        print("No matching disease found.")


def add_sample():
    image_name = input("Enter image filename (example: leaf_06.jpg): ").strip()
    disease = input("Enter disease label (example: Healthy): ").strip()

    if not image_name or not disease:
        print("Both fields are required.")
        return

    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["image_name", "disease"])
        writer.writerow([image_name, disease])

    print("Sample added successfully.")


def main():
    while True:
        records = load_data()
        print("\n===== Potato Disease Dataset Explorer =====")
        print("1. View dataset summary")
        print("2. Search disease")
        print("3. Add a sample record")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_summary(records)
        elif choice == "2":
            search_disease(records)
        elif choice == "3":
            add_sample()
        elif choice == "4":
            print("Thank you for using the project!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

from src.data_stream import fetch_data
from src.data_cleaning import clean_data
from src.model_training import train_model
from src.utils import print_header

def main():
    print_header("Step 1: Fetching Data")
    fetch_data()

    print_header("Step 2: Cleaning Data")
    clean_data()

    print_header("Step 3: Training Model")
    train_model()

    print("\n✅ Pipeline completed successfully.")

if __name__ == "__main__":
    main()

import pandas as pd
import os

def clean_data():
    """
    Loads raw data, performs initial cleaning, and saves the cleaned data
    into the 'data/processed' directory.
    """
    # --- 1. Define File Paths ---
    # The paths are relative to the root of your project folder.
    # The 'src' folder is where this script is located.
    # We need to go up one level (..) to access the 'data' folder.
    print("Defining file paths...")
    crop_data_path = 'data/raw/crop_yield.csv'
    climate_data_path = 'data/raw/climate.csv'
    co2_data_path = 'data/raw/co2.csv'
    
    # --- 2. Load the Raw Data ---
    print("Loading raw data from 'data/raw'...")
    try:
        crop_df = pd.read_csv(crop_data_path)
        climate_df = pd.read_csv(climate_data_path)
        co2_df = pd.read_csv(co2_data_path)
        print("Raw data loaded successfully.")

    except FileNotFoundError as e:
        print(f"Error: One of the data files was not found. Please check your folder structure. Details: {e}")
        return

    # --- 3. Initial Data Inspection ---
    print("\n--- Initial Data Info ---")
    print("Crop Yield Data Info:")
    crop_df.info()
    print("\nClimate Data Info:")
    climate_df.info()
    print("\nCO2 Data Info:")
    co2_df.info()

    # --- 4. Clean the Climate Data ---
    print("\n--- Cleaning Climate Data ---")
    # Drop rows where 'AverageTemperature' is missing (NaN)
    initial_rows = len(climate_df)
    climate_df.dropna(subset=['AverageTemperature'], inplace=True)
    rows_dropped = initial_rows - len(climate_df)
    print(f"Dropped {rows_dropped} rows with missing 'AverageTemperature'.")

    # Convert the 'dt' column to a proper datetime object
    climate_df['dt'] = pd.to_datetime(climate_df['dt'])
    print("'dt' column converted to datetime.")

    # Display the cleaned climate data info to confirm changes
    print("\nCleaned Climate Data Info:")
    climate_df.info()

    # --- 5. Prepare Other DataFrames (No major cleaning needed for this step) ---
    print("\n--- Processing other dataframes ---")
    print("Crop and CO2 dataframes are ready for the next step.")

    # --- 6. Save the Cleaned Data ---
    print("\nSaving cleaned data to 'data/processed'...")
    processed_dir = 'data/processed'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
        print(f"Created directory: {processed_dir}")
    
    # Save the cleaned dataframes to CSV files
    crop_df.to_csv(os.path.join(processed_dir, 'cleaned_crop_yield.csv'), index=False)
    climate_df.to_csv(os.path.join(processed_dir, 'cleaned_climate.csv'), index=False)
    co2_df.to_csv(os.path.join(processed_dir, 'cleaned_co2.csv'), index=False)

    print("All cleaned data saved successfully. You're ready for the next step: EDA! 🚀")

# Execute the function when the script is run
if __name__ == "__main__":
    clean_data()
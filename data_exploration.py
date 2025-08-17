# Step 3: Basic Data Cleaning & Exploration

# --- Crop Data ---
print("\nCrop Data Info:")
print(crop_data.info())
print("\nMissing values in Crop Data:")
print(crop_data.isnull().sum())

# --- Climate Data ---
print("\nClimate Data Info:")
print(climate_data.info())
print("\nMissing values in Climate Data:")
print(climate_data.isnull().sum())

# Convert 'dt' column in climate dataset to datetime
climate_data['dt'] = pd.to_datetime(climate_data['dt'], errors='coerce')

# --- CO2 Data ---
print("\nCO2 Data Info:")
print(co2_data.info())
print("\nMissing values in CO2 Data:")
print(co2_data.isnull().sum())

# Ensure Year column is numeric
co2_data['Year'] = pd.to_numeric(co2_data['Year'], errors='coerce')

# Remove invalid years (like negative ones)
co2_data = co2_data[co2_data['Year'] > 0]

print("\nCO2 Data after cleaning invalid years:")
print(co2_data.head())

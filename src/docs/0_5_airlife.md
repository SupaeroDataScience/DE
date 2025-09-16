# Extract, Transform, Load (ETL) - AirLife Workshop

## Overview

In this 3-hour hands-on workshop, you will build a proof-of-concept ETL pipeline for **AirLife**, a startup that tracks aircraft lifecycle data including flight history, carbon footprint, and real-time location. You'll work through the complete ETL process from API data extraction to database loading, gaining practical experience with real-world data engineering challenges.

**Learning Objectives:**

- Understand ETL pipeline design and implementation
- Work with REST APIs for data extraction  
- Apply data transformation techniques using Python and SQL
- Implement data loading into PostgreSQL
- Use Git for collaborative development
- Document and present your ETL solution

**Prerequisites:**

- Basic understanding of Python programming
- Familiarity with SQL queries
- Git fundamentals
- Access to a development environment with Python 3.7+ and PostgreSQL

---

## Part 1: Understanding AirLife and Setup (30 minutes)

### 1.1 AirLife Company Overview (10 minutes)

**AirLife** is a startup that tracks basic information about aircraft and flights. For this workshop, we'll focus on a simple version of their data pipeline.

**Our Goal Today:**

- Extract airport data from a CSV file
- Extract some live flight data from a simple API
- Clean and combine this data 
- Load it into a PostgreSQL database

**Data Sources We'll Use:**

- **OpenFlights CSV**: Airport information (name, city, country, coordinates)
- **OpenSky Network API**: Current flights over Europe

### 1.2 Fork and Explore the Repository (10 minutes)

1. **Access the Starter Repository:** https://github.com/SupaeroDataScience/ETL-AirLife

2. **Fork the Repository:** 

    - Click "Fork" on the repository page
    - Clone your forked version locally:
    ```bash
    git clone https://github.com/YOUR_USERNAME/ETL-AirLife.git
    cd ETL-AirLife
    ```

3. **Explore Repository Structure:**
   ```
   ETL-AirLife/
   ├── README.md
   ├── requirements.txt
   ├── data/
   │   └── airports.csv (sample data provided)
   ├── src/
   │   ├── extract_data.py
   │   ├── transform_data.py
   │   └── load_data.py
   ├── database_setup.sql
   └── main.py
   ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 1.3 Quick API Test (10 minutes)

Let's test the OpenSky Network API to see what data looks like:

1. **Test the API:** Open a web browser and visit:
   ```
   https://opensky-network.org/api/states/all?lamin=45&lomin=5&lamax=50&lomax=15
   ```

2. **Understand the Response:** You'll see JSON data with current flights. Each flight has:

    - Aircraft identifier
    - Country of origin  
    - Longitude and latitude
    - Altitude and speed

3. **Note:** This API has rate limits, so we'll be careful not to call it too often!

---

## Part 2: Building the ETL Pipeline (120 minutes)

### 2.1 Database Setup (15 minutes)

First, let's create our PostgreSQL database and tables.

1. **Create Database:**
   ```bash
   # Connect to PostgreSQL
   psql -U your_username -d postgres
   ```

2. **Run Database Setup:**
   ```sql
   -- Create database
   CREATE DATABASE airlife_db;
   
   -- Connect to the new database
   \c airlife_db;
   
   -- Run the setup script
   \i database_setup.sql
   ```

3. **Verify Tables:** Check that your tables were created:
   ```sql
   SELECT * FROM airports LIMIT 5;
   ```

### 2.2 Data Extraction (35 minutes)

Now let's work on `src/extract_data.py`. This file will handle getting our data.

#### Extract Airport Data from CSV

Complete the function to read airport data:

```python
import pandas as pd
import requests
import time

def extract_airports():
    """Extract airport data from CSV file"""
    # TODO: Read the airports.csv file using pandas
    # TODO: Print how many airports were loaded
    # TODO: Return the DataFrame
    # The file is in data/airports.csv
    pass

def extract_flights():
    """Extract current flight data from OpenSky Network API"""
    url = "https://opensky-network.org/api/states/all"
    
    # Parameters to limit to Europe area
    params = {
        'lamin': 45,  # South boundary
        'lomin': 5,   # West boundary  
        'lamax': 50,  # North boundary
        'lomax': 15   # East boundary
    }
    
    try:
        # TODO: Make the API request using requests.get()
        # TODO: Check if the response is successful (status_code == 200)
        # TODO: Convert JSON response to pandas DataFrame
        # TODO: Return the DataFrame
        
        # HINT: response.json() gives you the data
        # HINT: The actual flight data is in response.json()['states']
        pass
        
    except Exception as e:
        print(f"Error fetching flight data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
```

#### Your Tasks:
1. **Complete `extract_airports()`:** Read the CSV file and return a pandas DataFrame
2. **Complete `extract_flights()`:** Make the API call and convert the response to a DataFrame
3. **Test Your Functions:** Run the extraction script to see if it works

### 2.3 Data Transformation (35 minutes)

Open `src/transform_data.py` and work on cleaning our data:

```python
import pandas as pd

def clean_airports(airports_df):
    """Clean airport data"""
    print(f"Starting with {len(airports_df)} airports")
    
    # TODO: Remove rows with missing latitude or longitude
    # TODO: Remove airports with invalid coordinates
    # TODO: Print how many airports remain after cleaning
    
    return airports_df

def clean_flights(flights_df):
    """Clean flight data"""
    if flights_df.empty:
        print("No flight data to clean")
        return flights_df
    
    print(f"Starting with {len(flights_df)} flights")
    
    # The OpenSky API returns data as a list of lists
    # We need to give it proper column names
    columns = ['icao24', 'callsign', 'origin_country', 'time_position', 
               'last_contact', 'longitude', 'latitude', 'altitude', 
               'on_ground', 'velocity', 'true_track', 'vertical_rate']
    
    # TODO: Assign column names to the DataFrame
    # TODO: Remove flights with missing coordinates
    # TODO: Convert altitude from meters to feet (multiply by 3.28084)
    # TODO: Print how many flights remain after cleaning
    
    return flights_df

def combine_data(airports_df, flights_df):
    """Combine airport and flight data for analysis"""
    # For this simple exercise, we'll just return both DataFrames
    # In a real system, you might join them based on proximity
    
    return airports_df, flights_df
```

#### Your Tasks:
1. **Complete the cleaning functions:** Remove invalid data and fix data types
2. **Test Your Transformations:** Make sure your cleaned data looks correct
3. **Handle Edge Cases:** What happens if there's no flight data? Make sure your code doesn't crash

### 2.4 Data Loading (35 minutes)

Finally, let's load our data into PostgreSQL. Open `src/load_data.py`:

```python
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def load_to_database(airports_df, flights_df):
    """Load cleaned data into PostgreSQL database"""
    
    # TODO: Create connection string
    # Format: postgresql://username:password@localhost:5432/airlife_db
    connection_string = "postgresql://your_username:your_password@localhost:5432/airlife_db"
    
    try:
        # TODO: Create SQLAlchemy engine
        engine = create_engine(connection_string)
        
        # TODO: Load airports data
        # TODO: Load flights data (only if not empty)
        
        print("Data loaded successfully!")
        
        # TODO: Print some basic statistics
        # How many airports were loaded?
        # How many flights were loaded?
        
    except Exception as e:
        print(f"Error loading data: {e}")

def verify_data():
    """Check that data was loaded correctly"""
    connection_string = "postgresql://your_username:your_password@localhost:5432/airlife_db"
    
    try:
        engine = create_engine(connection_string)
        
        # TODO: Query the database to verify data

        airports_count = pd.read_sql("SELECT COUNT(*) FROM airports", engine)
        print(f"Airports in database: {airports_count.iloc[0,0]}")
        
        flights_count = pd.read_sql("SELECT COUNT(*) FROM flights", engine) 
        print(f"Flights in database: {flights_count.iloc[0,0]}")

        # TODO: Show sample data
        sample_airports = pd.read_sql("SELECT * FROM airports LIMIT 3", engine)
        print("Sample airports:")
        print(sample_airports)

    except Exception as e:
        print(f"Error verifying data: {e}")
```

#### Your Tasks:
1. **Update Connection String:** Use the correct database credentials
2. **Complete the Loading Functions:** Use pandas to_sql() to load data
3. **Test the Pipeline:** Run the verification function to make sure it worked

---

## Part 3: Putting It All Together (30 minutes)

### 3.1 Complete the Main Pipeline (15 minutes)

Now let's connect all our pieces in `main.py`:

```python
#!/usr/bin/env python3
"""
AirLife ETL Pipeline - Simple Version
"""

from src.extract_data import extract_airports, extract_flights
from src.transform_data import clean_airports, clean_flights, combine_data
from src.load_data import load_to_database, verify_data

def main():
    """Run the complete ETL pipeline"""
    print("Starting AirLife ETL Pipeline...")
    
    # Step 1: Extract data
    print("\n=== EXTRACTION ===")
    airports = extract_airports()
    flights = extract_flights()
    
    # Step 2: Transform data
    print("\n=== TRANSFORMATION ===")
    clean_airports_data = clean_airports(airports)
    clean_flights_data = clean_flights(flights)
    final_airports, final_flights = combine_data(clean_airports_data, clean_flights_data)
    
    # Step 3: Load data
    print("\n=== LOADING ===")
    load_to_database(final_airports, final_flights)
    
    # Step 4: Verify everything worked
    print("\n=== VERIFICATION ===")
    verify_data()
    
    print("\n✅ ETL Pipeline completed!")

if __name__ == "__main__":
    main()
```

#### Your Tasks:
1. **Test the Full Pipeline:** Run `python main.py` and fix any errors
2. **Handle Missing Data:** What happens if the API call fails? Make sure your pipeline still works
3. **Add Basic Logging:** Add print statements to track progress

### 3.2 Simple Documentation and Git Commit (15 minutes)

#### Update Your README

Create a simple README.md explaining:

```markdown
# AirLife ETL Pipeline

## What This Does
This pipeline extracts airport data from a CSV file and live flight data from an API, 
cleans the data, and loads it into a PostgreSQL database.

## How to Run It
1. Install dependencies: `pip install -r requirements.txt`
2. Set up PostgreSQL database
3. Update database connection in `src/load_data.py`
4. Run: `python main.py`

## What We Built
- **Extract:** Gets airport data from CSV and flight data from OpenSky Network API
- **Transform:** Cleans invalid coordinates and converts units
- **Load:** Puts clean data into PostgreSQL tables

## Team Members
- [Add your names here]
```

#### Commit Your Work

You should save your progress to Git often:

```bash
# Add all your changes
git add CHANGED_FILENAMES

# Commit with a descriptive message
git commit -m "MESSAGE HERE"

# Push to your forked repository
git push origin main
```

---

## Workshop Deliverables

By the end of this 3-hour workshop, you should have:

### ✅ **Working Pipeline** 
- Extracts airport data from CSV
- Fetches live flight data from API  
- Cleans and validates the data
- Loads everything into PostgreSQL

### ✅ **Code Repository**
- All Python files completed with your solutions
- Basic README documentation
- Code committed to Git

### ✅ **Database with Data**
- PostgreSQL tables with actual airport and flight data
- Able to run simple queries on your data

## Quick Demo (If Time Allows)

If you finish early, try these simple queries on your data:

```sql
-- How many airports do we have?
SELECT COUNT(*) FROM airports;

-- Show airports in France
SELECT name, city FROM airports WHERE country = 'France' LIMIT 5;

-- How many flights are currently active?
SELECT COUNT(*) FROM flights;

-- Show the highest flying aircraft
SELECT callsign, altitude FROM flights 
WHERE altitude IS NOT NULL 
ORDER BY altitude DESC LIMIT 3;
```

## What We've Covered

- **ETL Basics:** Extract, Transform, Load workflow
- **API Integration:** Making HTTP requests and handling JSON responses  
- **Data Cleaning:** Handling missing values and invalid data
- **Database Loading:** Using pandas to insert data into PostgreSQL
- **Error Handling:** Making code robust when things go wrong

## Next Steps

This workshop prepares you for the larger [ETL Project](0_4_project.md) where you'll design your own startup's ETL pipeline with more complex requirements, better error handling, and features that showcase the value points of your startup.
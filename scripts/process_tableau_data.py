#!/usr/bin/env python3

import json
import pandas as pd
import sys
import os
from datetime import datetime

# Get file paths from environment variables or use defaults
input_file = os.environ.get('INPUT_FILE', 'raw_failure_data.json')
output_csv = os.environ.get('OUTPUT_CSV', 'processed_failure_data.csv')
output_json = os.environ.get('OUTPUT_JSON', 'processed_failure_data.json')

print(f"Processing data from {input_file}...")

try:
    # Load the raw JSON data
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Data validation steps
    print("Starting data validation...")

    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        print(f"WARNING: Found {missing_values.sum()} missing values:")
        print(missing_values[missing_values > 0])

    # Check for duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"WARNING: Found {duplicates} duplicate rows")
        df = df.drop_duplicates()
        print("Duplicates removed")

    # Structure validation (example - adjust for your data schema)
    required_columns = ['id', 'timestamp', 'error_code', 'description']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"ERROR: Missing required columns: {missing_columns}")
        sys.exit(1)

    # Generate metadata
    metadata = {
        "extraction_time": datetime.now().isoformat(),
        "record_count": len(df),
        "columns": list(df.columns),
        "missing_values_count": int(missing_values.sum()),
        "duplicates_removed": int(duplicates)
    }
    
    # Save metadata
    with open(os.path.join(os.path.dirname(output_json), "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

    # Save processed data
    df.to_csv(output_csv, index=False)
    df.to_json(output_json, orient='records')

    print("Data processing complete!")
    print(f"Processed {len(df)} records")
    print(f"Data saved to {output_csv} and {output_json}")

    sys.exit(0)
    
except Exception as e:
    print(f"ERROR: {str(e)}")
    sys.exit(1) 
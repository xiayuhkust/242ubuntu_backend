#!/usr/bin/env python3
import pandas as pd
import sys

def compare_excel_files(original_file, processed_file):
    """Compare original and processed Excel files to verify Twitter ID extraction"""
    # Read Excel files
    original_df = pd.read_excel(original_file)
    processed_df = pd.read_excel(processed_file)
    
    print(f"Original columns: {list(original_df.columns)}")
    print(f"Processed columns: {list(processed_df.columns)}")
    
    # Check if Twitter_user_id column exists in processed file
    if 'Twitter_user_id' not in processed_df.columns:
        print("❌ Twitter_user_id column not found in processed file")
        return False
    
    # Check if Twitter_user_id values are numeric
    numeric_ids = 0
    total_ids = 0
    
    print("\nTwitter ID Check:")
    for index, row in processed_df.iterrows():
        if pd.notna(row.get('Twitter_user_id')):
            total_ids += 1
            try:
                int(row['Twitter_user_id'])
                numeric_ids += 1
                print(f"✅ Row {index}: {row['Name']} - ID: {row['Twitter_user_id']} (numeric)")
            except ValueError:
                print(f"❌ Row {index}: {row['Name']} - ID: {row['Twitter_user_id']} (not numeric)")
    
    if total_ids == 0:
        print("❌ No Twitter IDs found in processed file")
        return False
    
    success_rate = (numeric_ids / total_ids) * 100 if total_ids > 0 else 0
    print(f"\nNumeric IDs: {numeric_ids}/{total_ids} ({success_rate:.1f}%)")
    
    if success_rate == 100:
        print("✅ All Twitter IDs are numeric")
        return True
    else:
        print("❌ Some Twitter IDs are not numeric")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} original_file.xlsx processed_file.xlsx")
        sys.exit(1)
    
    original_file = sys.argv[1]
    processed_file = sys.argv[2]
    
    success = compare_excel_files(original_file, processed_file)
    sys.exit(0 if success else 1)

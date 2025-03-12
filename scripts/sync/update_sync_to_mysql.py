#!/usr/bin/env python3
"""
Script to update the sync_to_mysql.py script to include kol_character synchronization.
This script adds the necessary code to sync_to_mysql.py to enable kol_character synchronization.
"""

import os
import sys
import re
import logging
import argparse
import shutil
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def backup_file(file_path):
    """Create a backup of the file"""
    backup_path = f"{file_path}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}"
    try:
        shutil.copy2(file_path, backup_path)
        logging.info(f"Created backup of {file_path} at {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Error creating backup of {file_path}: {str(e)}")
        return None

def update_sync_to_mysql(file_path):
    """Update the sync_to_mysql.py script to include kol_character synchronization"""
    try:
        # Read the file
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Create a backup
        backup_file(file_path)
        
        # Add import statement
        import_pattern = r'(from scripts\.sync\.sync_kol_tweet import run_kol_tweet_sync.*)'
        import_replacement = r'\1\nfrom scripts.sync.sync_kol_character import run_kol_character_sync  # Add kol_character sync import'
        
        content = re.sub(import_pattern, import_replacement, content)
        
        # Add run_kol_character_sync function
        function_pattern = r'(def run_kol_tweet_sync.*?return False\n)(.*)'
        function_replacement = r'\1\ndef run_kol_character_sync(limit=None, test=False):\n    """Run the KOL character synchronization script"""\n    logging.info("Starting KOL character synchronization")\n    \n    cmd = ["python3", "scripts/sync/sync_kol_character.py"]\n    \n    if limit:\n        cmd.extend(["--limit", str(limit)])\n    \n    if test:\n        cmd.append("--test")\n    \n    start_time = time.time()\n    \n    try:\n        result = subprocess.run(\n            cmd,\n            check=True,\n            stdout=subprocess.PIPE,\n            stderr=subprocess.PIPE,\n            universal_newlines=True\n        )\n        \n        logging.info(f"KOL character synchronization completed in {time.time() - start_time:.2f} seconds")\n        logging.info(f"Output: {result.stdout}")\n        \n        if result.stderr:\n            logging.warning(f"Errors: {result.stderr}")\n        \n        return True\n    \n    except subprocess.CalledProcessError as e:\n        logging.error(f"KOL character synchronization failed: {e}")\n        logging.error(f"Output: {e.stdout}")\n        logging.error(f"Errors: {e.stderr}")\n        return False\n\2'
        
        content = re.sub(function_pattern, function_replacement, content, flags=re.DOTALL)
        
        # Add call to run_kol_character_sync in main function
        main_pattern = r'(    # Run KOL tweet sync\n    if args\.kol_tweet or args\.all:\n        run_kol_tweet_sync\(args\.limit, args\.test\)\n)'
        main_replacement = r'\1\n    # Run KOL character sync\n    if args.kol_character or args.all:\n        run_kol_character_sync(args.limit, args.test)\n'
        
        content = re.sub(main_pattern, main_replacement, content)
        
        # Add command-line argument for kol_character
        parser_pattern = r'(    parser\.add_argument\("--kol-tweet", action="store_true", help="Sync KOL tweets"\)\n)'
        parser_replacement = r'\1    parser.add_argument("--kol-character", action="store_true", help="Sync KOL character data")\n'
        
        content = re.sub(parser_pattern, parser_replacement, content)
        
        # Write the updated content back to the file
        with open(file_path, 'w') as f:
            f.write(content)
        
        logging.info(f"Updated {file_path} to include kol_character synchronization")
        return True
    except Exception as e:
        logging.error(f"Error updating {file_path}: {str(e)}")
        return False

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Update sync_to_mysql.py to include kol_character synchronization')
    parser.add_argument('--file-path', type=str, default='/home/ubuntu/nitterlocal/scripts/sync/sync_to_mysql.py', help='Path to the sync_to_mysql.py file')
    
    args = parser.parse_args()
    
    # Update the sync_to_mysql.py script
    update_sync_to_mysql(args.file_path)

if __name__ == "__main__":
    main()

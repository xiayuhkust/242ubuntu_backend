#!/usr/bin/env python3
# test_twitter_id.py
import sys
import os

# Add the app directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.twitter_utils import get_user_id_from_twitter_handle

# Test handles
test_handles = ["elonmusk", "BillGates", "BarackObama", "taylorswift13"]

print("Testing Twitter ID extraction:")
for handle in test_handles:
    user_id = get_user_id_from_twitter_handle(handle)
    print(f"Handle: {handle}, User ID: {user_id}")
    
    # Verify it's a numeric ID
    try:
        int(user_id)
        print(f"✅ ID is numeric")
    except ValueError:
        print(f"❌ ID is not numeric: {user_id}")

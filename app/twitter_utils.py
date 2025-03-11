"""
Twitter utility functions for extracting Twitter IDs from URLs.
This module provides utility functions for working with Twitter URLs.
"""

import os
import sys
import logging
import re
import subprocess
import tempfile
import json
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_twitter_handle(url):
    """Extract Twitter handle from a URL (works with both nitter.net and twitter.com)"""
    if not url:
        return None
    
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        
        # Check if it's a Twitter URL
        if 'twitter.com' in parsed_url.netloc:
            domain = 'twitter.com'
        elif 'x.com' in parsed_url.netloc:
            domain = 'x.com'
        else:
            return None
        
        # Extract the handle from the path
        path_parts = parsed_url.path.strip('/').split('/')
        if not path_parts:
            return None
        
        handle = path_parts[0]
        return handle.lower()
    except Exception as e:
        logging.error(f"Error extracting Twitter handle from {url}: {str(e)}")
        return None

def get_user_id_from_twitter_handle(handle, client_dir=None):
    """
    Get user ID from Twitter handle using a simplified approach
    
    This is a simplified version that doesn't require the full Twitter client setup.
    For production use, you would integrate with the full TwitterScraper class.
    """
    if not handle:
        return None
    
    try:
        # For now, we'll just return the handle as the ID
        # In a production environment, you would use the TwitterScraper class
        logging.info(f"Simplified mode: Using handle as user ID for {handle}")
        return handle
        
    except Exception as e:
        logging.error(f"Error getting user ID for handle {handle}: {str(e)}")
        return handle  # Fall back to using the handle as the user ID

def process_twitter_urls(urls):
    """
    Process a list of Twitter URLs and extract their user IDs
    
    Args:
        urls (list): List of Twitter URLs to process
        
    Returns:
        list: List of dictionaries with URL and user_id
    """
    results = []
    
    for url in urls:
        try:
            # Extract Twitter handle
            handle = extract_twitter_handle(url)
            
            # Get user ID from handle
            user_id = get_user_id_from_twitter_handle(handle) if handle else None
            
            results.append({
                "url": url,
                "handle": handle,
                "user_id": user_id,
                "status": "success" if user_id else "error",
                "error": None if user_id else "Could not extract user ID"
            })
            
        except Exception as e:
            logging.error(f"Error processing URL {url}: {str(e)}")
            results.append({
                "url": url,
                "handle": None,
                "user_id": None,
                "status": "error",
                "error": str(e)
            })
    
    return results

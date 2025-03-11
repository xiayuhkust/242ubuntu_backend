import requests
import os
import json
import pandas as pd
import tempfile

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_health_endpoint():
    """Test the health check endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✅ Health endpoint test passed")

def test_process_twitter_urls_endpoint():
    """Test the process Twitter URLs endpoint"""
    urls = [
        "https://twitter.com/elonmusk",
        "https://twitter.com/BillGates",
        "https://x.com/satyanadella"
    ]
    
    response = requests.post(
        f"{BASE_URL}/api/process-twitter-urls",
        json=urls
    )
    
    assert response.status_code == 200
    result = response.json()
    assert result["total"] == 3
    assert result["successful"] >= 2
    
    # Check that the results contain the expected fields
    for url_result in result["results"]:
        assert "url" in url_result
        assert "handle" in url_result
        assert "user_id" in url_result
        assert "status" in url_result
    
    print("✅ Process Twitter URLs endpoint test passed")

def test_excel_upload_and_processing():
    """Test the Excel file upload and processing endpoints"""
    # Create a sample Excel file
    df = pd.DataFrame({
        "Name": ["User1", "User2", "User3"],
        "Twitter": [
            "https://twitter.com/elonmusk",
            "https://twitter.com/BillGates",
            "https://x.com/satyanadella"
        ]
    })
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as temp:
        temp_path = temp.name
        df.to_excel(temp_path, index=False)
    
    try:
        # Upload the Excel file
        with open(temp_path, "rb") as f:
            files = {"file": (os.path.basename(temp_path), f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
            upload_response = requests.post(f"{BASE_URL}/api/upload-excel", files=files)
        
        assert upload_response.status_code == 200
        upload_result = upload_response.json()
        assert "filename" in upload_result
        
        # Process the Excel file
        process_data = {"file_id": upload_result["filename"]}
        process_response = requests.post(f"{BASE_URL}/api/process-excel", data=process_data)
        
        assert process_response.status_code == 200
        process_result = process_response.json()
        assert "processed_file" in process_result
        assert "results" in process_result
        assert "total_urls" in process_result["results"]
        assert process_result["results"]["total_urls"] == 3
        
        # Try to download the processed file
        download_response = requests.get(f"{BASE_URL}/api/download/{process_result['processed_file']}")
        assert download_response.status_code == 200
        
        print("✅ Excel upload and processing test passed")
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

def run_tests():
    """Run all tests"""
    print("Running API tests...")
    
    try:
        test_health_endpoint()
        test_process_twitter_urls_endpoint()
        test_excel_upload_and_processing()
        
        print("All tests passed! ✅")
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")

if __name__ == "__main__":
    run_tests()

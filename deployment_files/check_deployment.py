#!/usr/bin/env python3
"""
Script untuk mengecek status deployment Streamlit.io
"""
import requests
import time
import sys

def check_streamlit_deployment(url):
    """Check if Streamlit deployment is working"""
    try:
        print(f"Checking deployment at: {url}")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("✅ Deployment berhasil!")
            print(f"Status Code: {response.status_code}")
            print(f"Content Length: {len(response.text)} bytes")
            
            # Check if it's a Streamlit app
            if "streamlit" in response.text.lower() or "st-emotion-cache" in response.text:
                print("✅ Detected Streamlit app")
            else:
                print("⚠️  Not a Streamlit app or not fully loaded")
                
            return True
        else:
            print(f"❌ Deployment failed with status: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False

def generate_example_urls():
    """Generate example Streamlit.io URLs"""
    import random
    import string
    
    examples = []
    for i in range(3):
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
        url = f"https://streamflow-{random_part}.streamlit.app"
        examples.append(url)
    
    return examples

if __name__ == "__main__":
    print("🎥 StreamFlow Deployment Checker")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
        check_streamlit_deployment(url)
    else:
        print("Contoh URL yang akan didapat setelah deployment:")
        examples = generate_example_urls()
        for i, url in enumerate(examples, 1):
            print(f"{i}. {url}")
        
        print("\nUntuk check deployment, jalankan:")
        print("python check_deployment.py <URL_STREAMLIT_APP>")
        print("\nContoh:")
        print(f"python check_deployment.py {examples[0]}")
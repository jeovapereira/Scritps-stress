import requests
import time

def test_latency(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    latency = end_time - start_time
    print(f"Latency for {url}: {latency} seconds")

# Example usage
test_latency("https://www.example.com")
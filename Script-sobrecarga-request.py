import requests
import threading

def send_request(url):
    while True:
        response = requests.get(url)
        # You can add additional logic here to process the response if needed

# Example usage
url = "https://www.example.com"
num_threads = 10

# Create and start multiple threads to send requests concurrently
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_request, args=(url,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
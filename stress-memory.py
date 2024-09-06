import ctypes

def allocate_memory(size_mb):
    # Calculate the number of bytes to allocate
    size_bytes = size_mb * 1024 * 1024

    # Allocate memory using ctypes
    buffer = ctypes.create_string_buffer(size_bytes)

    # Fill the allocated memory with data
    for i in range(size_bytes):
        buffer[i] = b'A'

    # Keep the script running to maintain memory usage
    while True:
        pass

# Example usage
allocate_memory(100)
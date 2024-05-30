import hashlib
import timeit
import matplotlib.pyplot as plt

def measure_md5_time(data):
    return timeit.timeit(lambda: hashlib.md5(data).hexdigest(), number=10000)

def measure_sha256_time(data):
    return timeit.timeit(lambda: hashlib.sha256(data).hexdigest(), number=10000)

md5_times = []
sha256_times = []
string_lengths = []

base_string = "a"

for length in range(1, 1001):  
    data = base_string * length
    md5_time = measure_md5_time(data.encode())
    sha256_time = measure_sha256_time(data.encode())
    
    md5_times.append(md5_time)
    sha256_times.append(sha256_time)
    string_lengths.append(length)

plt.figure(figsize=(10, 5))
plt.plot(string_lengths, md5_times, label='MD5', color='blue')
plt.plot(string_lengths, sha256_times, label='SHA256', color='green')
plt.xlabel('String Length (characters)')
plt.ylabel('Accumulated Time (seconds)')
plt.title('MD5 vs SHA256 Hashing Speed with Increasing String Length')
plt.legend()
plt.show()
import hashlib
import timeit
import matplotlib.pyplot as plt
import os

medium_data = os.urandom(1024 * 1024)  # 1 MB
large_data = os.urandom(1024 * 1024 * 100)  # 100 MB
extra_large_data = os.urandom(1024 * 1024 * 200)  # 200 MB

def measure_md5_time(data):
    return timeit.timeit(lambda: hashlib.md5(data).hexdigest(), number=10)

def measure_sha256_time(data):
    return timeit.timeit(lambda: hashlib.sha256(data).hexdigest(), number=10)

data_sizes = ['1 MB', '100 MB', '200 MB']
data_list = [medium_data, large_data, extra_large_data]

md5_times = []
sha256_times = []

for data in data_list:
    md5_times.append(measure_md5_time(data))
    sha256_times.append(measure_sha256_time(data))

plt.figure(figsize=(10, 5))
bar_width = 0.35

positions = list(range(len(data_sizes)))
bar_positions_md5 = [p - bar_width/2 for p in positions]
bar_positions_sha256 = [p + bar_width/2 for p in positions]

plt.bar(bar_positions_md5, md5_times, width=bar_width, color='blue', align='center', label='MD5')
plt.bar(bar_positions_sha256, sha256_times, width=bar_width, color='green', align='center', label='SHA256')

plt.xlabel('Data Size')
plt.ylabel('Accumulated Time (seconds)')
plt.title('MD5 vs SHA256 Hashing Speed with Different Data Sizes')
plt.xticks(ticks=positions, labels=data_sizes)
plt.legend()
plt.show()
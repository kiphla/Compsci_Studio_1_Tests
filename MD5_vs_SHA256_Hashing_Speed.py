import hashlib
import timeit
import matplotlib.pyplot as plt

data = b"The quick brown fox jumps over the lazy dog" * 1000  

def hash_md5():
    hashlib.md5(data).hexdigest()

def hash_sha256():
    hashlib.sha256(data).hexdigest()

md5_time = timeit.timeit(hash_md5, number=10000)
sha256_time = timeit.timeit(hash_sha256, number=10000)

hash_algorithms = ['MD5', 'SHA256']
times = [md5_time, sha256_time]

plt.figure(figsize=(10, 5))
plt.bar(hash_algorithms, times, color=['blue', 'green'])
plt.xlabel('Hash Algorithm')
plt.ylabel('Time (seconds)')
plt.title('MD5 vs SHA256 Hashing Speed')
plt.show()
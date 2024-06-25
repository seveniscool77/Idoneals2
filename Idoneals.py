import time
import math
from concurrent.futures import ProcessPoolExecutor, as_completed

# Get the input value
N = int(input('What value would you want to test up to: '))

# Initialize an empty set for unique combinations
ABC_Set = set()
idoneal = []

# Start timing
start_time = time.time()

def ABC_Combinations(N, start, end, total_combinations, current_combinations):
    result_set = set()
    for a in range(start, end):
        for b in range(a + 1, 3 * N):
            for c in range(b + 1, 3 * N + 1):
                result_set.add(a * b + b * c + a * c)
                current_combinations += 1
    return result_set, current_combinations

# Define the number of chunks and the range for each chunk
num_chunks = 4
chunk_size = (3 * N - 1) // num_chunks
ranges = [(i * chunk_size + 1, (i + 1) * chunk_size + 1) for i in range(num_chunks)]
if ranges[-1][1] < 3 * N - 1:
    ranges[-1] = (ranges[-1][0], 3 * N - 1)

# Calculate total combinations for progress tracking
total_combinations = sum((end - start) * (3 * N - start) * (3 * N - start + 1) // 2
                         for start, end in ranges)

current_combinations = 0

# Use ProcessPoolExecutor for parallel processing
with ProcessPoolExecutor() as executor:
    futures = [executor.submit(ABC_Combinations, N, start, end, total_combinations, current_combinations)
               for start, end in ranges]
    for future in as_completed(futures):
        ABC_Set.update(future.result()[0])
        current_combinations = future.result()[1]

# Convert the set to a list and sort it
ABC_List = sorted(ABC_Set)

print('\nBeginning list check')

def check_idoneal(N, List, idoneal):
    max_value = 3 * N ** 2 + 1
    list_index = 0
    list_length = len(List)

    for i in range(1, max_value):
        while list_index < list_length and List[list_index] < i:
            list_index += 1
        if list_index >= list_length or List[list_index] > i:
            idoneal.append(i)
    return idoneal

# Check for idoneal numbers
check_idoneal(N, ABC_List, idoneal)

# Print the idoneal list
print(idoneal)


# Time checking
end = time.time() - start_time
print(end)

#if end >= 60 * 60 * 24:
    #print(f"Program completed in {end / (60 * 60 * 24):.2f} days")
#elif end >= 60 * 60:
   # print(f"Program completed in {end / (60 * 60):.2f} hours")
#elif end >= 60:
  #  print(f"Program completed in {end / 60:.2f} minutes")
#else:
 #   print(f"Program completed in {end:.2f} seconds")

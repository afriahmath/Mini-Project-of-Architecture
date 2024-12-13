def best_fit(memory_blocks, process_sizes):
    allocation = [-1] * len(process_sizes)  # Initialize all processes as unallocated

    for i, process in enumerate(process_sizes):
        best_index = -1
        for j, block in enumerate(memory_blocks):
            if block >= process:
                if best_index == -1 or memory_blocks[best_index] > block:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            memory_blocks[best_index] -= process

    return allocation

# Input data
memory_blocks = list(map(int, input("Enter the sizes of memory blocks (space-separated): ").split()))
process_sizes = list(map(int, input("Enter the sizes of processes (space-separated): ").split()))

# Run the algorithm
allocation_result = best_fit(memory_blocks.copy(), process_sizes)

# Display results
print("\nProcess No.\tProcess Size\tBlock No.")
for i, process in enumerate(process_sizes):
    if allocation_result[i] != -1:
        print(f"{i + 1}\t\t{process}\t\t{allocation_result[i] + 1}")
    else:
        print(f"{i + 1}\t\t{process}\t\tNot Allocated")
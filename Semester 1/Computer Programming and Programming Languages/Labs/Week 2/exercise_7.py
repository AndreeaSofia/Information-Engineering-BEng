from collections import deque

def generate_list_using_queue(n):
    M = []
    queue = deque([1])  # Start with 1 in the queue

    while len(M) < n:
        # Get the next number from the queue
        x = queue.popleft()
        M.append(x)
        
        # Generate new numbers using the rules
        new_number1 = 2 * x + 1
        new_number2 = 3 * x + 1
        
        # Add the new numbers to the queue
        queue.append(new_number1)
        queue.append(new_number2)

    return M
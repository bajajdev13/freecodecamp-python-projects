def hanoi_solver(n):
    # Initialize the three rods
    rods = [list(range(n, 0, -1)), [], []]
    states = []
    
    def format_state():
        return f"{rods[0]} {rods[1]} {rods[2]}"
    
    # Record the initial state
    states.append(format_state())
    
    def move(k, source, target, aux):
        if k > 0:
            # Move k-1 disks from source to auxiliary rod
            move(k-1, source, aux, target)
            
            # Move the largest disk from source to target rod
            disk = rods[source].pop()
            rods[target].append(disk)
            
            # Record the state after moving the disk
            states.append(format_state())
            
            # Move the k-1 disks from auxiliary rod to target rod
            move(k-1, aux, target, source)

    # Start the recursion to move n disks from rod 0 to rod 2, using rod 1 as auxiliary
    move(n, 0, 2, 1)
    
    # Return all states separated by newlines
    return "\n".join(states)

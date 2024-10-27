import numpy as np
import queue
import matplotlib.pyplot as plt


def generate_interarrival_times(rate, size):
    return np.random.exponential(1/rate, size)


def generate_service_times(rate, size):
    return np.random.exponential(1/rate, size)


def simulate_queue(arrival_rate, service_rate, num_customers):
    interarrival_times = generate_interarrival_times(arrival_rate, num_customers)
    service_times = generate_service_times(service_rate, num_customers)
    
    q = queue.Queue()
    arrival_times = np.cumsum(interarrival_times)
    service_start_times = [0] * num_customers
    departure_times = [0] * num_customers
    
    current_time = 0
    for i in range(num_customers):
        if not q.empty():
            current_time = max(current_time, arrival_times[i])
        
        q.put(i)
        
        if i == 0 or current_time >= departure_times[i-1]:
            service_start_times[i] = arrival_times[i]
        else:
            service_start_times[i] = departure_times[i-1]
        
        departure_times[i] = service_start_times[i] + service_times[i]
        q.get()
    
    return arrival_times, service_start_times, departure_times


def analyze_queue(arrival_times, service_start_times, departure_times):
    wait_times = service_start_times - arrival_times
    queue_lengths = []
    
    for t in np.linspace(0, max(departure_times), 1000):
        queue_lengths.append(sum((arrival_times <= t) & (departure_times > t)))
    
    avg_wait_time = np.mean(wait_times)
    avg_queue_length = np.mean(queue_lengths)
    
    return avg_wait_time, avg_queue_length, queue_lengths


def plot_queue(queue_lengths):
    plt.figure(figsize=(10, 5))
    plt.plot(queue_lengths, label='Queue Length')
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Queue Length Over Time')
    plt.legend()
    plt.show()


def model(): 
    # Parameters
    arrival_rate = 10  # customers per unit time
    service_rate = 1  # customers per unit time
    num_customers = 100000

    # Simulate and analyze the queue
    arrival_times, service_start_times, departure_times = simulate_queue(arrival_rate, service_rate, num_customers)
    avg_wait_time, avg_queue_length, queue_lengths = analyze_queue(arrival_times, service_start_times, departure_times)

    # Print results
    print(f"Average wait time: {avg_wait_time:.2f}")
    print(f"Average queue length: {avg_queue_length:.2f}")

    # Plot results
    plot_queue(queue_lengths)



import numpy as np
import queue
import matplotlib.pyplot as plt

def generate_interarrival_times(rate, size):
    return np.random.exponential(1/rate, size)


def generate_service_times(rate, size):
    return np.random.exponential(1/rate, size)


def generate_bursty_demand(total_time, base_rate, burst_rate, burst_duration, burst_interval):
    """
    Generate bursty demand using Poisson distribution.
    
    :param total_time: Total simulation time.
    :param base_rate: Base Poisson rate during non-burst periods.
    :param burst_rate: Poisson rate during burst periods.
    :param burst_duration: Duration of each burst period.
    :param burst_interval: Interval between bursts.
    :return: A list of event times representing the bursty demand.
    """
    times = []
    current_time = 0
    
    while current_time < total_time:
        # Determine if it's a burst period
        if (current_time // burst_interval) % 2 == 1:
            rate = burst_rate
        else:
            rate = base_rate
        
        # Generate the next event time
        interarrival_time = np.random.exponential(1 / rate)
        current_time += interarrival_time
        
        if current_time < total_time:
            times.append(current_time)
    
    return times


def simulate_queue_with_bursty_demand(demand_times, service_rate):
    num_customers = len(demand_times)
    service_times = generate_service_times(service_rate, num_customers)
    
    q = queue.Queue()
    service_start_times = [0] * num_customers
    departure_times = [0] * num_customers
    
    current_time = 0
    for i in range(num_customers):
        if not q.empty():
            current_time = max(current_time, demand_times[i])
        
        q.put(i)
        
        if i == 0 or current_time >= departure_times[i-1]:
            service_start_times[i] = demand_times[i]
        else:
            service_start_times[i] = departure_times[i-1]
        
        departure_times[i] = service_start_times[i] + service_times[i]
        q.get()
    
    return demand_times, service_start_times, departure_times


def plot_queue(queue_lengths):
    plt.figure(figsize=(10, 5))
    plt.plot(queue_lengths, label='Queue Length')
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Queue Length Over Time')
    plt.legend()
    plt.show()


def plot_bursty_demand(demand, total_time):
    plt.figure(figsize=(10, 5))
    plt.hist(demand, bins=np.arange(0, total_time + 1, 1), alpha=0.75, edgecolor='black')
    plt.xlabel('Time')
    plt.ylabel('Number of Events')
    plt.title('Bursty Demand Over Time')
    plt.show()


def analyze_queue(arrival_times, service_start_times, departure_times):
    wait_times = service_start_times - arrival_times
    queue_lengths = []
    
    for t in np.linspace(0, max(departure_times), 1000):
        queue_lengths.append(sum((arrival_times <= t) & (departure_times > t)))
    
    avg_wait_time = np.mean(wait_times)
    avg_queue_length = np.mean(queue_lengths)
    
    return avg_wait_time, avg_queue_length, queue_lengths


def model():
    # Parameters
    total_time = 1000  # Total simulation time
    base_rate = 1  # Base rate (events per unit time) during non-burst periods
    burst_rate = 10  # Rate during burst periods
    burst_duration = 50  # Duration of each burst period
    burst_interval = 200  # Interval between bursts (including burst duration)

    # Generate bursty demand
    bursty_demand = generate_bursty_demand(total_time, base_rate, burst_rate, burst_duration, burst_interval)

    plot_bursty_demand(bursty_demand, total_time)

    # Parameters for service rate
    service_rate = 6  # customers per unit time
    arrival_rate = 10  # customers per unit time
    num_customers = 100000

    # Simulate the queue with bursty demand
    arrival_times, service_start_times, departure_times = simulate_queue_with_bursty_demand(bursty_demand, service_rate)
    avg_wait_time, avg_queue_length, queue_lengths = analyze_queue(arrival_times, service_start_times, departure_times)

    # Print results
    print(f"Average wait time: {avg_wait_time:.2f}")
    print(f"Average queue length: {avg_queue_length:.2f}")

    # Plot results
    plot_queue(queue_lengths)

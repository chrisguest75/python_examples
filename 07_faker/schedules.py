import logging
from faker import Faker

def generate_schedules() -> int:
    """test function"""
    logger = logging.getLogger()

    faker = Faker()
    # Generating a set of start and end times
    times = [(faker.time(), faker.time()) for _ in range(5)]

    # Sorting each pair so that the earlier time is the start time
    sorted_times = [(min(start, end), max(start, end)) for start, end in times]

    return sorted_times



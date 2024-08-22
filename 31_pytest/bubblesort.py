from typing import List


def sort(values: List[int]) -> List[int]:
    if len(values) <= 1:
        return values

    for i in range(len(values)):
        for j in range(i, len(values)):
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]

    return values

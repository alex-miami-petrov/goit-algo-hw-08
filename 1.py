import heapq


def min_cost(lengths):
    if not lengths:
        return 0
    if len(lengths) == 1:
        return 0
    
    heapq.heapify(lengths)
    total_cost = 0


    while len(lengths) > 1:
        L1 = heapq.heappop(lengths)
        L2 = heapq.heappop(lengths)

        current_cost = L1 + L2
        total_cost += current_cost

        heapq.heappush(lengths, current_cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 8, 10, 2, 6, 20]
    cost = min_cost(cables)

    print(f"Min: {cost}")

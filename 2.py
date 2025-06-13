import heapq


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]


def merge(lists):
    heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i , 0))

    merged_list = []


    while heap:
        val, list_i, el_i = heapq.heappop(heap)
        merged_list.append(val)

        if el_i + 1 < len(lists[list_i]):
            next_val = lists[list_i][el_i + 1]
            heapq.heappush(heap, (next_val, list_i, el_i + 1))

    return merged_list



# if __name__ == "__main__":
#     res = merge(lists)
#     print(res)

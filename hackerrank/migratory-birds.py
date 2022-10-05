def migratoryBirds(arr):
    max_element = max(arr)
    list_freq = [0]*(max_element+1)
    for bird_id in set(arr):
        list_freq[bird_id] += arr.count(bird_id)

    return list_freq.index(max(list_freq))

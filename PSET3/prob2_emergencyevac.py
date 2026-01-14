def min_boats(weights, limit):
    weights.sort()

    left = 0
    right = len(weights) - 1
    boats = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1   # light person used
        right -= 1      # heavy person always used
        boats += 1

    return boats
weights = [3, 2, 2, 1]
limit = 3

print("Minimum boats needed:", min_boats(weights, limit))

def bagpack(bagpack_size, weight, values, n):
    print(f'bagpack size: {bagpack_size}')
    print(f'weight: {weight}')
    print(f'values: {values}')
    print(f'n: {n}')
    if n == 0 or bagpack_size == 0:
        return 0
    
    if weight[n - 1] > bagpack_size:
        return bagpack(bagpack_size, weight, values, n - 1)

    print(f'first value: {values[n - 1] + bagpack(bagpack_size - weight[n - 1], weight, values, n - 1)}')
    print(f'second value: {bagpack(bagpack_size, weight, values, n - 1)}')
    return max(values[n - 1] + bagpack(bagpack_size - weight[n - 1], weight, values, n - 1), bagpack(bagpack_size, weight, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weight = [10, 20, 30]
    bagpack_size = 50
    n = len(values)

    result = bagpack(bagpack_size, weight, values, n)
    print(result)
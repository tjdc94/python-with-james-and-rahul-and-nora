l = [4, 2, 1, 3, 5]

def bubble(nums: list[int]) -> list[int]:
    """
    complexity: 0(n^2)

    - compare 2 adjacent numbers
    - swap if lhs > rhs
    - move to next number, repeat above step
    - do this till the end of the list 
    - repeat this till size - i - 1
    """
    size = len(nums)

    for i in range(0, size):
        for j in range(0, size - i - 1):
            if nums [j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

def group_by(nums: list[int], predicate) -> tuple[list[int], list[int]]:
    satisfies, doesnt = [], []

    for n in nums:
        if predicate(n):
            satisfies.append(n)
        else: 
            doesnt.append(n)
    return satisfies, doesnt


def quick(nums: list[int]) -> list[int]:
    """
    complexity: 
        best case: 0(nlog2(n))
        avg case: 0(nlog2(n))
        worst case: 0(n^2)

    [4, 2, 1, 3, 5]

    pivot = 4

    lesser = [2, 1, 3]
    greater = [5]

    sort([2, 1, 3]) + [4] + sort([5])

    sort([1]) + [2] + sort([3]) + [4] + [5]

    [1] + [2] + [3] + [4] + [5]
    """
    if len(nums) <= 1:
        return nums
    
    pivot, rest = nums[0], nums[1:]
    lesser, greater = group_by(rest, lambda x: x < pivot)
    # lesser = [n for n in rest if n < pivot]
    # greater = [n for n in rest if n >= pivot]

    return quick(lesser) + [pivot] + quick(greater)


if __name__ == "__main__": #Ask about this line
    print(bubble(l))
    print(quick([4,2,1,3,4,5,2]))


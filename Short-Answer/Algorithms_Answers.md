#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I think this would be O(n) runtime because it grows at the same rate of whatever 'n' is. For example, if n = 2 then the while loop would always run if a what less than 8 (2*2*2) as well as if it was true, a would be a + a contstant 4 (2*2)


b) This is a O(n log n) because even though that in the second loop it is multiplying j by 2, the second loop will only run if j is less than n. If j starts at 1 but gets multiplied by two each time it's less than whatever n is, then it grows pretty fast. (Even if the first loop says to go in the range of n times)


c) This would be O(n) because even if bunnies has a different amount in them each time, the function will return bunnies * 2 each time to figure out total bunny ears.

## Exercise II

If n equals an array (or list) that has the amount of stories in them, I would do a binary search method that would be O(n log n) because every time you're searching if the middle story is the egg breaking method, you eliminate half the list. Or, dividing it in 2 each time until we find the correct story.

For example: 
##I have a building with 10 stories
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_if_broken(n, floor_dropped):
    lowest_floor = n[0]
    highest_floor = n[-1]

    while lowest_floor <= highest_floor:
        middle_floor = lowest_floor + highest_floor // 2
        if floor_dropped < middle_floor:
            highest_floor = middle_floor - 1
        elif floor_dropped > middle_floor:
            lowest_floor = middle_floor + 1
        else:
            return middle_floor
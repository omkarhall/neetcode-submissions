class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
            boats += 1
        return boats
                
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        number_of_boats = 0
        i = 0
        j =len(people)-1
        people.sort()
        while i <= j:
            while j > i and people[i] + people[j] > limit:
                number_of_boats += 1
                j -= 1
            number_of_boats += 1
            i += 1
            j -= 1
        return number_of_boats
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p , s in zip(position , speed)]
        pair.sort(reverse = True)
        print(pair)

        stack = []
        for p , s in pair:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1]  <= stack[-2]:
                stack.pop()

        return len(stack)          






"""
group the cars based on time 
so if two cars are going to take the same time to reach dest -> same car fleet
we will create a key,pair list of car:speed grouped in descending order
"""

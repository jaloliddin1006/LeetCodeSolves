class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Create a dictionary to store the frequency of values
        frequency_dict = Counter(nums)
        
        # Step 2: Sort the array based on frequency using a custom sorting key
        sorted_nums = sorted(nums, key=lambda x: (frequency_dict[x], -x))
        
        # Step 3: Return the sorted array
        return sorted_nums
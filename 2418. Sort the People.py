class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict = dict(zip(heights, names))
        name = []
        for i in dict(sorted(my_dict.items())):
            name.append(my_dict[i])
        return name[::-1] 
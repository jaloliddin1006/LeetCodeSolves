class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        my_list = []
        for r in image:
            row = []
            for i in r:
                row.insert(0, int(not i))
            my_list.append(row)
        return my_list
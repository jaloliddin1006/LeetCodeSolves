import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mydict = {}
        mydict_ = {}

        for i in ransomNote:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] += 1
        for j in magazine:
            if j in mydict:
                if j not in mydict_:
                    mydict_[j] = 1
                elif mydict_[j] == mydict[j]:
                    continue
                else:
                    mydict_[j] += 1

        return mydict== mydict_
           

# print(Solution().canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))


print("effjfggbffjdgbjjhhdegh".count("f"))
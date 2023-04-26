class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address
        return address.replace(".", "[.]")
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Replace all '.' with '[.]'
        return address.replace('.', '[.]')
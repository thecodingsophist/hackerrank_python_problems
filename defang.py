"""
Take an IP address and replace the periods with [.]
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        split_address = list(address)
        print(split_address)
        defanged = ""
        for char in split_address:
            if char == ".":
                defanged += "[.]"
            else:
                defanged += char
        return defanged

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = ''.join(map(str, digits))
        integer = int(number_str) + 1
        return self.int_to_list(integer)

    def int_to_list(self, number):
        return [int(digit) for digit in str(number)]
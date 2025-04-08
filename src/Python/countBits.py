class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        
        for i in range(n + 1):
            # Convert to binary, remove '0b' prefix
            byte = bin(i)[2:]
            # Add spaces between each bit
            spaced = ' '.join(byte)
            print(f"{i}: {spaced}")  # Optional: print number and spaced binary string
            # Count number of 1s
            count = byte.count('1')
            bits.append(count)
        
        return bits
            
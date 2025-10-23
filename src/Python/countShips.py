# Definition for a Sea and Point provided by the platform
# class Sea:
#     def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#         pass
# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # Invalid rectangle
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1

        mid_x = (bottomLeft.x + topRight.x) // 2
        mid_y = (bottomLeft.y + topRight.y) // 2

        count = 0
        count += self.countShips(sea, Point(mid_x, mid_y), bottomLeft)                      # bottom-left
        count += self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y+1))  # top-left
        count += self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x+1, bottomLeft.y))  # bottom-right
        count += self.countShips(sea, topRight, Point(mid_x+1, mid_y+1))                      # top-right
        return count
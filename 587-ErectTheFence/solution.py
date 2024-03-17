# Sort, 2-D math
Point = List[int]

class Solution:
    
    def is_convex(self, p1: Point, p2: Point, p3: Point):
      assert p1[0] <= p2[0] <= p3[0] or p1[0] >= p2[0] >= p3[0]
      if p3[0] == p1[0]:
        return True
      interpolated_p2_y = p1[1] + (p3[1] - p1[1]) / (p3[0] - p1[0]) * (p2[0] - p1[0])
      return (interpolated_p2_y == p2[1]) or ((interpolated_p2_y < p2[1]) == (p3[0] > p1[0]))
    
    def outerTrees(self, trees: [Point]) -> [Point]:
        points = sorted(trees)
        up_border_points = []
        for p in points:
          while len(up_border_points) >= 2:
            if self.is_convex(up_border_points[-2], up_border_points[-1], p):
              break
            else:
              up_border_points.pop()
          up_border_points.append(p)
        down_border_points = []
        for p in points[::-1]:
          while len(down_border_points) >= 2:
            if self.is_convex(down_border_points[-2], down_border_points[-1], p):
              break
            else:
              down_border_points.pop()
          down_border_points.append(p)
        unique_points = set((p[0], p[1]) for p in up_border_points + down_border_points) 
        return list(unique_points)

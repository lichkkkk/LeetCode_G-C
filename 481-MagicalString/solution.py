class Solution:

  def __init__(self) -> None:
    self.magical_string = [1, 2, 2]
    self.one_count = [1, 1, 1]
    self.max_len = 100_000
    curr_pos = 2
    curr_num = 1
    while len(self.magical_string) < self.max_len:
      curr_one_count = self.one_count[-1]
      repeat_times = self.magical_string[curr_pos]
      self.magical_string.extend([curr_num] * repeat_times)
      if curr_num == 1:
        self.one_count.extend(list(range(curr_one_count+1, curr_one_count+repeat_times+1)))
      else:
        self.one_count.extend([curr_one_count] * repeat_times)
      curr_pos += 1
      curr_num = 3 - curr_num

  def magicalString(self, n: int) -> int:
    return self.one_count[n-1]

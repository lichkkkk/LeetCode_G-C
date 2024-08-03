class Solution:

  def is_equal_to(self, num, target):
    return abs(num - target) < 1e-5

  def get_valid_ops(self, num1, num2):
    if self.is_equal_to(num2, 0):
      return ('+', '*')
    else:
      return ('+', '-', '*', '/')

  def calculate(self, num1, num2, op):
    match op:
      case '+': return num1 + num2
      case '-': return num1 - num2
      case '*': return num1 * num2
      case '/': return num1 / num2

  def reduce(self, cards):
    res = set()
    for i in range(len(cards) - 1):
      for j in range(i+1, len(cards)):
        remaining_nums = [cards[k] for k in range(len(cards)) if k not in (i, j)]
        for num1, num2 in [(cards[i], cards[j]), (cards[j], cards[i])]:
          for op in self.get_valid_ops(num1, num2):
            calculated_num = self.calculate(num1, num2, op)
            res.add(tuple(remaining_nums + [calculated_num]))
    return res

  def judgePoint24(self, init_cards: List[int]) -> bool:
    all_cards = [init_cards]

    # reduce 3 times
    for _ in range(3):
      new_all_cards = set()
      for in_cards in all_cards:
        out_cards = self.reduce(in_cards)
        new_all_cards |= out_cards
      all_cards = new_all_cards

    # check all res
    for cards in all_cards:
      assert len(cards) == 1
      num = list(cards)[0]
      if self.is_equal_to(num, 24):
        return True
    return False

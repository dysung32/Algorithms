function computeWhenDouble(interestRate) {
  let money = 1
  let cntYear = 0

  while (money < 2) {
    cntYear += 1
    money = money * (1 + interestRate / 100)
  }
  return cntYear
}
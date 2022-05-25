function getLongestElement(arr) {
  return arr.reduce((acc, cur) => {
    if (cur.length > acc.length) {
      acc = cur
    }
    return acc
  }, "")
}
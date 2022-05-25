function getLengthOfLongestElement(arr) {
  let result = arr.reduce((acc, cur) => {
    if (cur.length > acc.length) {
      acc = cur
    }
    return acc
  }, "")
  return result.length
}
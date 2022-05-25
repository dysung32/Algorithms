function getIndex(arr, num) {
  const IsSmallThan = function (el) {
    return el < num
  }
  const result = arr.filter((el) => IsSmallThan(el))
  return result.length
}
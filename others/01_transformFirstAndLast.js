function transformFirstAndLast(arr) {
  let obj = {}
  if (arr.length === 0) {
    return obj
  }
  obj[arr[0]] = arr.slice(-1)[0]
  return obj
}
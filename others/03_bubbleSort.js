const bubbleSort = function (arr) {
  let len = arr.length
  for (let i = 0; i < len; i++) {
    let swaps = 0
    for (let j = 0; j < len - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        swaps++
        let tmp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = tmp
      }
    }
    if (swaps === 0) {
      break
    }
  }
  return arr
}

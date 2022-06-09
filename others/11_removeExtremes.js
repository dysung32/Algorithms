function removeExtremes(arr) {
  let shortestIdx = 0
  let shortestLen = 20
  let longestIdx = 0
  let longestLen = 0
  for(let i = 0; i < arr.length; i++) {
    if (arr[i].length <= shortestLen) {
      shortestLen = arr[i].length
      shortestIdx = i
    }
    if (arr[i].length >= longestLen) {
      longestLen = arr[i].length
      longestIdx = i
    }
  }

  let newArr = []
  for(let idx=0; idx < arr.length; idx++) {
    if (idx !== shortestIdx && idx !== longestIdx) {
      newArr.push(arr[idx])
    }
  }

  return newArr
}

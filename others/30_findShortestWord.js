function findShortestWord(arr) {
  let filteredArr = arr.filter(el => typeof el === 'string')

  if (filteredArr.length === 0) {
    return ""
  }

  return filteredArr.reduce((acc, cur) => {
    if (cur.length < acc.length) {
      acc = cur
    }
    return acc
  })
}
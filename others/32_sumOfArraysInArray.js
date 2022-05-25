function sumOfArraysInArray(arr) {
  const singleArray = arr.reduce((acc, cur) => acc.concat(cur), [])
  const filteredSingleArray = singleArray.filter(el => typeof(el) === 'number')
  return filteredSingleArray.reduce((acc, cur) => {
    return acc + cur
  }, 0)
}
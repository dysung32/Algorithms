function filterCallback(func, arr) {
  let result = []
  for(let el of arr) {
    if (func(el) === true) {
      result.push(el)
    }
  }
  return result
}
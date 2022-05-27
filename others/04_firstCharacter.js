function firstCharacter(str) {
  let strArr = str.split(' ')
  let firstWords = ''
  if (str.length === 0) {
    return firstWords
  }
  for(let i in strArr) {
    firstWords = firstWords + strArr[i][0]
  }
  return firstWords
}
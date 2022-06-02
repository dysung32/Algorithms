function convertDoubleSpaceToSingle(str) {
  let resultStr = ''
  let before = ''
  let now = ''
  for (let i=0; i<str.length; i++) {
    now = str[i]
    if (before !== ' ' || now !== ' ') {
      resultStr += str[i]
    }
    before = now
  }
  return resultStr
}
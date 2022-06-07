function ABCheck(str) {
  let abCnt = 0
  str = str.toLowerCase()
  let strLen = str.length

  for(let i=0; i<str.length; i++) {
    if (str[i] === 'a' && i+4 < strLen - 1) {
      if (str[i+4] === 'b') {
        abCnt += 1
      }
    } else if (str[i] === 'b' && i+4 < strLen - 1) {
      if (str[i+4] === 'a') {
        abCnt += 1
      }
    }
  }

  if (abCnt > 0) {
    return true
  }
  return false
}

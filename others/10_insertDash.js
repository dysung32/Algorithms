function insertDash(str) {
  let newStr = ''
  let preStr = -1
  for (let i=0; i<str.length; i++) {
    if (str[i] % 2 === 1 && preStr % 2 === 1) {
      newStr += `-${str[i]}`
    } else {
      newStr += str[i]
    }
    preStr = str[i]
  }
  return newStr
}
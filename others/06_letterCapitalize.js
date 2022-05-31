function letterCapitalize(str) {
  let strToArr = str.split(' ')
  for(let i = 0; i < strToArr.length; i++) {
    if (strToArr[i][0] >= 'a' && strToArr[i][0] <= 'z') {
      strToArr[i] = strToArr[i].replace(strToArr[i][0], strToArr[i][0].toUpperCase())
    }
  }
  return strToArr.join(' ')
}
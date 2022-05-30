function firstReverse(str) {
  const arr = [...str]

  let arr_reversed = arr.reverse()

  let str_reversed = ''
  for (let i = 0; i < arr_reversed.length; i++) {
    str_reversed += arr_reversed[i]
  }
  return str_reversed
}

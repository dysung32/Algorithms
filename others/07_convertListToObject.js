function convertListToObject(arr) {
  let obj = {}
  for (let i=0; i < arr.length; i++) {
    for (let j=0; j < arr[i].length; j++) {
      if (arr[i][0] in obj) {
        continue
      } else {
        obj[arr[i][0]] = arr[i][1]
      }
    }
  }
  return obj
}
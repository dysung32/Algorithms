function mapCallback(func, arr) {
  let result = []
  for(let i=0; i < arr.length; i++) {
    result.push(func(arr[i]))
  }
  return result;
}
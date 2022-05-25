function square(number) {
  return number * number
}

function getSquaredElementsAtProperty(obj, property) {
  let value = obj[property]
  if (Array.isArray(value) === true) {
    return value.map(square)
  }
  return []
}

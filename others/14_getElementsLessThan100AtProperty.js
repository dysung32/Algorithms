function lessThan100(number) {
  return number < 100;
}

function getElementsLessThan100AtProperty(obj, property) {
  if (Array.isArray(obj[property]) === true) {
    return obj[property].filter(el => {
      if (typeof(el) === 'number') {
        return lessThan100(el)
      }})
  }
  return []
}

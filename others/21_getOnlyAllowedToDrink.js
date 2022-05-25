function getOnlyAllowedToDrink(arr) {
  const moreThan18 = function(obj) {
    return obj.age >= 18
  }
  let arrMoreThan18 = arr.filter(moreThan18)

  const getName = function(obj) {
    return obj.name
  }
  return arrMoreThan18.map(getName)
}
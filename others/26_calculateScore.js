function calculateScore(records, value) {
  return records.reduce((acc,cur) => {
    if (cur.animal === value) {
      return acc + cur.score
    } else {
      return acc
    }
  }, 0)
}
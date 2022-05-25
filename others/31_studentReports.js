function studentReports(students) {
  return students.reduce((acc, cur) => {
    if(cur.gender === 'female') {
      cur.grades = getAverage(cur.grades)
      acc.push(cur)
    }
    return acc
  },[])

}

function getAverage(args) {
  return args.reduce((acc, cur) => {
    return acc + cur
  }, 0) / (args.length)
}
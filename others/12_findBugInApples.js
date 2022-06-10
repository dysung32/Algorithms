function findBugInApples(arr) {
  for (let row = 0; row < arr.length; row++) {
    for (let col = 0; col < arr[row].length; col++) {
      if (arr[row][col] === 'B') {
        return [row, col]
      }
    }
  }
}

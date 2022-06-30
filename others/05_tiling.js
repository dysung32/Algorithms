let tiling = function (n) {
  const memo = [0, 1, 2];

  const aux = (size) => {
    if (memo[size] !== undefined) return memo[size];
    if (size <= 2) return memo[n];
    memo[size] = aux(size - 1) + aux(size - 2);
    return memo[size];
  };
  return aux(n);
};

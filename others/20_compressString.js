function compressString(str) {
  let result = ''
  let pre_str = str[0]
  let cnt = 1

  str = str + ' ';
  for (let i=1; i<str.length; i++) {
    if (pre_str === str[i]) {
      cnt++;
    } else {
      if (cnt >= 3) {
        result = result + `${cnt}${pre_str}`;
      } else {
        result = result + pre_str.repeat(cnt);
      }
      pre_str = str[i];
      cnt = 1;
    }
  }
  return result
}

function getDist(a, b) {
    return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);
}

function solution(numbers, hand) {
    let answer = '';
    const keypad = {
      1:[0,3], 2:[1,3], 3:[2,3],
      4:[0,2], 5:[1,2], 6:[2,2],
      7:[0,1], 8:[1,1], 9:[2,1],
      '*':[0,0], 0:[1,0], '#':[2,0],
  }

    let left = [1,4,7];
    let right = [3,6,9];
    let center = [2,5,8,0];

    let L_now = keypad['*'];
    let R_now = keypad['#'];

    let L_dist = 0;
    let R_dist = 0;

    let len = numbers.length;

    for(let i=0;i<len;i++) {
        let num = numbers[i];
        if(left.includes(num)) { // 1,4,7 일 때
            answer += 'L';
            L_now = keypad[num];
        } else if (right.includes(num)) { // 3,6,9 일 때
            answer += 'R';
            R_now = keypad[num];
        } else { // 2,5,8,0 중 하나일 때
            L_dist = getDist(keypad[num], L_now);
            R_dist = getDist(keypad[num], R_now);

            // 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용
            if (L_dist < R_dist) {
                answer += 'L';
                L_now = keypad[num];
            } else if (L_dist > R_dist) {
                answer += 'R';
                R_now = keypad[num];
            } else { // 만약 두 엄지손가락의 거리가 같다면
                if (hand == "right"){ // 오른손잡이는 오른손 엄지손가락 사용
                    answer += 'R';
                    R_now = keypad[num];
                }
                else if (hand == "left"){ // 왼손잡이는 왼손 엄지손가락 사용
                    answer += 'L';
                    L_now = keypad[num];
                }
            }
        }
    }
    return answer;
}
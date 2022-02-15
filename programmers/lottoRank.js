function solution(lottos, win_nums) {
    var answer = [];
    let max;
    let min;
    let cnt_win = 0;
    let cnt_zero = 0;

    for(let i=0;i<lottos.length;i++) {
        if(lottos[i] == 0)
            cnt_zero += 1;
    }
    for(let i=0;i<lottos.length;i++) {
        if(win_nums.includes(lottos[i])) {
            cnt_win += 1;
        }
    }

    min = checkRank(cnt_win);
    max = min - cnt_zero;

    if(cnt_zero == 6) {
        min = 6;
        max = 1;
    }
    answer = [max, min];
    return answer;
}
function checkRank(cnt_win) {
    if(cnt_win < 2){
        return 6;
    } else if (cnt_win == 2) {
        return 5;
    } else if (cnt_win == 3) {
        return 4;
    } else if (cnt_win == 4) {
        return 3;
    } else if (cnt_win == 5) {
        return 2;
    } else if (cnt_win == 6) {
        return 1;
    }
}
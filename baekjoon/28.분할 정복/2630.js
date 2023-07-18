const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map((el) => +el));
const [N] = input.shift();
// console.log("N: ", N);
// console.log("input: ", input);

const answer = [0, 0];

const func = (x, y, n) => {
  const checked = input[x][y];
  // console.log("x, y, n: ", x, y, n);
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (checked !== input[i][j]) {
        n /= 2;
        // console.log("n: ", n);
        func(x, y, n);
        func(x, y + n, n);
        func(x + n, y, n);
        func(x + n, y + n, n);
        return;
      }
    }
  }
  if (checked === 0) {
    // console.log("흰색: ", input[x][y]);
    answer[0] += 1;
  } else if (checked === 1) {
    // console.log("검정색: ", input[x][y]);
    answer[1] += 1;
  }
};

func(0, 0, N);
console.log(answer[0]);
console.log(answer[1]);

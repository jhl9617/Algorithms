const input1 = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map((el) => +el));
const [N] = input1.shift();
// console.log("N: ", N);
// console.log("input: ", input);

const answer = [0, 0, 0];

const func = (x, y, n) => {
  const checked = input1[x][y];
  //   console.log("x, y, n: ", x, y, n);
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (checked !== input1[i][j]) {
        n /= 3;
        // console.log("n: ", n);
        func(x, y, n);
        func(x, y + n, n);
        func(x, y + n * 2, n);
        func(x + n, y + n * 2, n);
        func(x + n, y, n);
        func(x + n * 2, y, n);
        func(x + n * 2, y + n, n);
        func(x + n, y + n, n);
        func(x + n * 2, y + n * 2, n);

        return;
      }
    }
  }
  if (checked === -1) {
    answer[0] += 1;
  } else if (checked === 0) {
    answer[1] += 1;
  } else if (checked === 1) {
    answer[2] += 1;
  }
};

func(0, 0, N);
console.log(answer[0]);
console.log(answer[1]);
console.log(answer[2]);

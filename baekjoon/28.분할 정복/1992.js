const input1 = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split("").map((el) => +el));
const [N] = input1.shift();

const answer = [];

// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// const input = [];
// let N;

// rl.on("line", function (line) {
//   if (!N) {
//     N = parseInt(line);
//   } else {
//     input.push(line.split("").map(Number));
//   }
// }).on("close", function () {
//   const answer = [];

const func = (x, y, n) => {
  const checked = input1[x][y];
  // console.log("x, y, n: ", x, y, n);
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (checked !== input1[i][j]) {
        n /= 2;

        answer.push("(");
        func(x, y, n);
        func(x, y + n, n);
        func(x + n, y, n);
        func(x + n, y + n, n);
        answer.push(")");
        return;
      }
    }
  }
  if (checked === 0) {
    answer.push("0");
  } else if (checked === 1) {
    answer.push("1");
  }
};

func(0, 0, N);

console.log(answer.join("").trim());
// });

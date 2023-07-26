const [A, B, C] = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(BigInt);

const pow = (A, B) => {
  // console.log("A, B: ", A, B);
  if (B === 1n) {
    console.log("A, B: ", A, B);

    return A % C;
  }
  const temp = pow(A, BigInt(parseInt(B / 2n)));
  console.log("temp: ", temp);

  if (B % 2n === 0n) {
    console.log("temp * temp: ", temp * temp);
    return (temp * temp) % C;
  } else {
    console.log("temp * temp * A: ", temp * temp * A);
    return (((temp * temp) % C) * A) % C;
  }
};

console.log(pow(A, B).toString());

//10^5 * 10^5 * 10 = 10^11
//10^1 * 10^1 * 10 * 10^1 * 10^1 * 10 * 10 = 10^5
// 10     10     10   10    10     10   10

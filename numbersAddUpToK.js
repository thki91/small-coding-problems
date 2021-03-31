// Given a list of numbers and a number k, return whether
// any two numbers from the list add up to k.
const numbersAddUpToK = (k, numbers) => {
  let addsUp = false;
  numbers.forEach((number, index) => {
    if (!addsUp) {
      const numbersLeft = [...numbers].slice(index + 1);
      numbersLeft.every(numberLeft => {
        addsUp = number + numberLeft === k;
        return (number + numberLeft) !== k; // continue if it doesn't add up
      });
    }
  });
  return addsUp;
};

const numbers = [10, 15, 3, 7, 1];
const k = 3;

console.log(numbersAddUpToK(k, numbers));

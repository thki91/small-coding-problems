// Given an array of integers, return a new array such that each element at
// index i of the new array is the product of all the numbers in the original
// array except the one at i.
const numbersProductsAtIndex = (numbers) => {
  return numbers.map((number, index) => {
    const numbersWithoutCurrentIndexNumber = [...numbers];
    numbersWithoutCurrentIndexNumber.splice(index, 1);
    return numbersWithoutCurrentIndexNumber.reduce((a, b) => a * b, 1);
  });
};

const numbers = [1, 2, 3, 4, 5];
console.log(numbersProductsAtIndex(numbers));

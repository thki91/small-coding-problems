// Given an array of integers, find the first missing
// positive integer in linear time and constant space
const firstMissingPositiveInteger = (numbers) => {
  const positiveNumbers = numbers.filter((num) => { return num >= 0 });
  const maxNumber = Math.max(...positiveNumbers);
  // first integer after max number as fallback/default value
  let firstPosInteger = maxNumber + 1;
  for(let i = maxNumber; i > 0; i --) {
    if (!positiveNumbers.includes(i)) {
      firstPosInteger = i;
    }
  }
  return firstPosInteger;
};

const numbers = [3, 4, -1, 1];
console.log(firstMissingPositiveInteger(numbers));

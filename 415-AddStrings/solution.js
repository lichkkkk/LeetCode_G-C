/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
  var result = [];
  var buffer = 0;
  for (i = 0; i <  Math.max(num1.length, num2.length); i++) {
    let sum = buffer + getDigit(num1, i) + getDigit(num2, i);
    let ones = sum % 10;
    let tens = (sum - ones) / 10;

    buffer = tens;
    result.push(ones.toString());
  }
  if (buffer != 0) {
    result.push(buffer.toString());
  }
  return result.reverse().join("");
}

function getDigit(num, index) {
  if (index < 0 || index >= num.length) {
    return 0;
  }
  return num.charAt(num.length - index - 1) - '0';
}

console.log(addStrings('123', '1234'));

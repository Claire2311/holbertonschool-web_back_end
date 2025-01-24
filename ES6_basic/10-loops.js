export default function appendToEachArrayValue(array, appendString) {
  for (const [i, el] of array.entries()) {
    array[i] = appendString + el;
  }
  return array;
}

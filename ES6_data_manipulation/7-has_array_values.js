export default function hasValuesFromArray(set, array) {
  let hasValuesFromArray = true;
  for (let i = 0; i < array.length; i++) {
    if (!set.has(array[i])) {
      hasValuesFromArray = false;
      break;
    }
  }
  return hasValuesFromArray;
}

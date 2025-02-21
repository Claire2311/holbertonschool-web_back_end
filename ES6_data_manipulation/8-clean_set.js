export default function cleanSet(set, startString) {
  if (startString === "") {
    return "";
  }

  const recherchedValue = [];
  set.forEach((value) => {
    if (value.startsWith(startString)) {
      recherchedValue.push(value.split(startString)[1]);
    }
  });
  console.log(recherchedValue);
  return recherchedValue.join("-");
}

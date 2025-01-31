export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      Promise.resolve({
        status: 200,
        body: "Success",
      });
    })
    .then(() => {
      console.log("Got a response from the API");
    })
    .catch(() => {
      return new Error();
    });
}

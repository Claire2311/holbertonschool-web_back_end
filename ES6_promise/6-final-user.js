import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  //   Promise.all([signUpUser, uploadPhoto]).then((values) => {
  //     console.log(values);
  //   });

  //   const p = Promise.all([signUpUser, uploadPhoto]);
  //   console.log(p);

  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((result) => ({
      status: result.status,
      value: result.status === "fulfilled" ? result.value : result.reason,
    }))
  );
}

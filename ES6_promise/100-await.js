import { uploadPhoto, createUser } from "./utils";

export default async function asyncUploadUser() {
  try {
    const photo = await Promise.try(uploadPhoto);

    const user = await Promise.try(createUser);
    return { photo, user };
  } catch {
    return {
      photo: null,
      user: null,
    };
  }
}

export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateName(name);
    this._length = this._validateLength(length);
    this._students = this._validateStudents(students);
  }

  _validateName(name) {
    if (typeof name !== "string") {
      throw new TypeError("Name must be a string");
    }
    return name;
  }

  _validateLength(length) {
    if (typeof length !== "number") {
      throw new TypeError("Length must be a string");
    }
    return length;
  }

  _validateStudents(students) {
    if (
      !Array.isArray(students) ||
      !students.every((student) => typeof student === "string")
    ) {
      throw new TypeError("Students must be an array of strings");
    }
    return students;
  }

  get name() {
    return this._name;
  }

  set name(str) {
    this._name = this._validateName(str);
  }

  get length() {
    return this._length;
  }

  set length(length) {
    this._length = this._validateLength(length);
  }

  get students() {
    return this._students;
  }

  set students(students) {
    this._students = this._validateStudents(students);
  }
}

// export default class HolbertonCourse {
//   constructor(name, length, students) {
//     this._name = this._validateName(name);
//     this._length = this._validateLength(length);
//     this._students = this._validateStudents(students);
//   }

//   // Validate name
//   _validateName(name) {
//     if (typeof name !== "string") {
//       throw new TypeError("Name must be a string");
//     }
//     return name;
//   }

//   // Validate length
//   _validateLength(length) {
//     if (typeof length !== "number") {
//       throw new TypeError("Length must be a number");
//     }
//     return length;
//   }

//   // Validate students
//   _validateStudents(students) {
//     if (
//       !Array.isArray(students) ||
//       !students.every((student) => typeof student === "string")
//     ) {
//       throw new TypeError("Students must be an array of strings");
//     }
//     return students;
//   }
//   // Getter and setter for name
//   get name() {
//     return this._name;
//   }

//   set name(name) {
//     this._name = this._validateName(name);
//   }

//   // Getter and setter for length
//   get length() {
//     return this._length;
//   }

//   set length(length) {
//     this._length = this._validateLength(length);
//   }

//   // Getter and setter for students
//   get students() {
//     return this._students;
//   }

//   set students(students) {
//     this._students = this._validateStudents(students);
//   }
// }

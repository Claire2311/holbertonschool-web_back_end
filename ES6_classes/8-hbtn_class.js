export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // When the class is cast into a Number, it should return the size.
  valueOf() {
    return this._size;
  }

  // When the class is cast into a String, it should return the location.
  toString() {
    return this._location;
  }
}

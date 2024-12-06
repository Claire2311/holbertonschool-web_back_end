const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("addition", () => {
  it("should return 3", () => {
    assert.strictEqual(calculateNumber(1, 2), 3);
  });
  it("should return 5", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it("should return 5", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});

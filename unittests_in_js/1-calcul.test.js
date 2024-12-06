const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("SUM", () => {
  it("should return 6", () => {
    assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
  });
});

describe("SUBSTRACT", () => {
  it("should return -4", () => {
    assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
  });
});

describe("DIVIDE", () => {
  it("should return 0.2", () => {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
  });
  it("should return Error", () => {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
  });
});

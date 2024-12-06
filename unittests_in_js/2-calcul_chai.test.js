const expect = require("chai").expect;
const calculateNumber = require("./2-calcul");

describe("SUM", () => {
  it("should return 6", () => {
    expect(calculateNumber("SUM", 1.4, 4.5)).be.equal(6);
  });
});

describe("SUBSTRACT", () => {
  it("should return -4", () => {
    expect(calculateNumber("SUBTRACT", 1.4, 4.5)).be.equal(-4);
  });
});

describe("DIVIDE", () => {
  it("should return 0.2", () => {
    expect(calculateNumber("DIVIDE", 1.4, 4.5)).be.equal(0.2);
  });
  it("should return Error", () => {
    expect(calculateNumber("DIVIDE", 1.4, 0)).be.equal("Error");
  });
});

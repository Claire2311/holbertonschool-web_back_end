const sinon = require("sinon");
const expect = require("chai").expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./5-payment");

describe("testsendPaymentRequestToApi", () => {
  it("should return 120", () => {
    const consoleSpy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith("The total is:", 120)).to.be.true;

    consoleSpy.restore();
  });

  it("should return 20", () => {
    const consoleSpy = sinon.spy(console, "log");

    sendPaymentRequestToApi(10, 10);

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith("The total is:", 20)).to.be.true;

    consoleSpy.restore();
  });
});

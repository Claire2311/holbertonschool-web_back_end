const sinon = require("sinon");
const expect = require("chai").expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./5-payment");

describe("testsendPaymentRequestToApi", () => {
  let consoleSpy = null;
  beforeEach(() => {
    consoleSpy = sinon.spy(console, "log");
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it("should return 120", () => {
    sendPaymentRequestToApi(100, 20);

    expect(consoleSpy.calledOnceWithExactly("The total is: 120")).to.be.true;
  });

  it("should return 20", () => {
    sendPaymentRequestToApi(10, 10);

    expect(consoleSpy.calledOnceWithExactly("The total is: 20")).to.be.true;
  });
});

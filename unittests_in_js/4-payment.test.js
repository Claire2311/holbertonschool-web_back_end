const sinon = require("sinon");
const expect = require("chai").expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("testsendPaymentRequestToApi", () => {
  it("should return the correct answer", () => {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);

    const consoleSpy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 200);

    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith("SUM", 100, 200)).to.be.true;

    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith("The total is:", 10)).to.be.true;

    stub.restore();
    consoleSpy.restore();
  });
});

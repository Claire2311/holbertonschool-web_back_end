const sinon = require("sinon");
const expect = require("chai").expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("testsendPaymentRequestToApi", () => {
  it("should be use one", () => {
    sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToApi(100, 200);
    expect(Utils.calculateNumber.withArgs("SUM", 100, 200).calledOnce).to.be
      .true;
    Utils.calculateNumber.restore();
  });
});

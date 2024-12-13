const sinon = require("sinon");
const expect = require("chai").expect;
const Utils = require("./utils");
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("getPaymentTokenFromAPI", () => {
  it("should resolve with the correct data when success is true", (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.deep.equal({ data: "Successful response from the API" });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });

  /* From chatGPT
  it("should do nothing when success is false", (done) => {
    // Since the promise does not resolve or reject when success is false,
    // we expect the test to complete without errors.
    getPaymentTokenFromAPI(false)
      .then(() => {
        // This block should not be reached
        done(new Error("Promise should not resolve when success is false."));
      })
      .catch(() => {
        // This block should also not be reached
        done(new Error("Promise should not reject when success is false."));
      });

    // Adding a slight delay to ensure nothing happens
    setTimeout(() => done(), 50);
  });*/
});

const request = require("request");
const expect = require("chai").expect;

describe("Cart page", () => {
  it("Content with number parameter", (done) => {
    request("http://localhost:7865/cart/12", (error, response, body) => {
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });

  it("Status with number parameter", function (done) {
    request("http://localhost:7865/cart/12", function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("Status with none number parameter", function (done) {
    request(
      "http://localhost:7865/cart/hello",
      function (error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      }
    );
  });
});

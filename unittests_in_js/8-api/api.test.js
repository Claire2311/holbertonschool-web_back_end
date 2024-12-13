const request = require("request");
const expect = require("chai").expect;

// const app = require("./api");

describe("Index page", () => {
  it("Content", (done) => {
    request("http://localhost:7865/", (error, response, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });

  it("Status", function (done) {
    request("http://localhost:7865/", function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
});

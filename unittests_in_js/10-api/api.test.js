const request = require("request");
const expect = require("chai").expect;

describe("Integration tests", () => {
  const options = {
    url: "http://localhost:7865/login",
    method: "POST",
    json: true,
    body: {
      userName: "Betty",
    },
  };
  it("Content with available_payments route", (done) => {
    request(
      "http://localhost:7865/available_payments",
      (error, response, body) => {
        expect(JSON.parse(body)).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false,
          },
        });
        done();
      }
    );
  });

  it("Status with available_payments route", function (done) {
    request(
      "http://localhost:7865/available_payments",
      function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        done();
      }
    );
  });

  it("Status with login route with no body", function (done) {
    request("http://localhost:7865/login", function (error, response, body) {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it("Status with login route with body", function (done) {
    request(options, function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("Content with login route with body", function (done) {
    request(options, function (error, response, body) {
      expect(body).to.equal("Welcome Betty");
      done();
    });
  });
});

import { createQueue } from "kue";
import { expect } from "chai";
import { sinon } from "sinon";

import createPushNotificationsJobs from "./8-job.js";

const queue = createQueue();

describe("createPushNotificationsJobs", () => {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it("display a error message if jobs is not an array", function () {
    const jobs = { foo: "bar" };
    expect(() => createPushNotificationsJobs(jobs, queue)).to.throw(
      Error,
      "Jobs is not an array"
    );
  });

  it("should not display a error message if jobs is an array", function () {
    const jobs = [];
    expect(() => createPushNotificationsJobs(jobs, queue)).to.not.throw();
  });

  it("create two new jobs to the queue", function () {
    const jobs = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "4153518743",
        message: "This is the code 4321 to verify your account",
      },
    ];
    expect(() => createPushNotificationsJobs(jobs, queue)).to.not.throw();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});

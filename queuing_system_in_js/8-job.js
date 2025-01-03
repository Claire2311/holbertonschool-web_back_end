const kue = require("kue");

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  for (const job of jobs) {
    const jobQueue = queue
      .create("push_notification_code_3", job)
      .save(function (err) {
        if (!err) console.log("Notification job created:", jobQueue.id);
      });

    jobQueue.on("complete", function () {
      console.log(`Notification job ${jobQueue.id} completed`);
    });

    jobQueue.on("failed", function (err) {
      console.log(`Notification job ${jobQueue.id} failed: ${err}`);
    });

    jobQueue.on("progress", function (progress) {
      console.log(`Notification job ${jobQueue.id} ${progress}% complete`);
    });
  }
}

module.exports = createPushNotificationsJobs;

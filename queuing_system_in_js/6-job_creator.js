const kue = require("kue");

const queue = kue.createQueue();

const jobDetail = {
  phoneNumber: "4153518780",
  message: "This is the code to verify your account",
};

const job = queue
  .create("push_notification_code", jobDetail)
  .save(function (err) {
    if (!err) console.log("Notification job created:", job.id);
  });

job.on("complete", function () {
  console.log("Notification job completed");
});

job.on("failed", function (errorMessage) {
  console.log("Notification job failed");
});

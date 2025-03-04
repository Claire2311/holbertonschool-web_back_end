import redis from "redis";

const client = redis.createClient();

client.on("error", (err) =>
  console.log("Redis client not connected to the server:", err)
);

client.on("connect", (stream) => {
  console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) console.log(err);
    console.log(reply);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

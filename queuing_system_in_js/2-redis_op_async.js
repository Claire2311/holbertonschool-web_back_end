import redis from "redis";
import { promisify } from "util";

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

function getValue(value) {
  client.get(value, (err, reply) => {
    if (err) console.log(err);
    console.log(reply);
  });
}

const getValuePromisify = promisify(getValue);

async function displaySchoolValue(schoolName) {
  await getValuePromisify(schoolName);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

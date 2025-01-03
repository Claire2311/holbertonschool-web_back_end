import { promisify } from "util";
import express from "express";
import redis from "redis";
import kue from "kue";

const client = redis.createClient();
client.on("error", (err) => console.error("Redis client error:", err));
client.on("connect", () => console.log("Connected to Redis server"));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const app = express();

app.use(express.json());

const port = 1245;
app.listen(port, (err) => {
  if (err) {
    console.error("Something bad happened");
  } else {
    reserveSeat(50);
    console.log(`App is listening on port ${port}`);
  }
});

async function reserveSeat(number) {
  await setAsync("available_seats", number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync("available_seats");
  return parseInt(seats, 10) || 0;
}

let reservationEnabled = true;

const queue = kue.createQueue();

app.get("/available_seats", async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get("/reserve_seat", async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservation are blocked" });
  }

  const job = queue.create("reserve_seat").save(function (err) {
    if (!err) {
      res.json({ status: "Reservation in process" });
    } else {
      return res.json({ status: "Reservation failed" });
    }
  });

  job.on("complete", function () {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on("failed", function (err) {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

app.get("/process", async (req, res) => {
  res.json({ status: "Queue processing" });

  queue.process("reserve_seat", async function (job, done) {
    try {
      const availableSeats = await getCurrentAvailableSeats();

      if (availableSeats <= 0) {
        reservationEnabled = false;
        return done(new Error("Not enough seats available"));
      }

      await reserveSeat(availableSeats - 1);

      if (availableSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    } catch (err) {
      done(err);
    }
  });
});

import { promisify } from "util";
import express from "express";
import { createClient } from "redis";

const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id) || null;
}

const app = express();

app.use(express.json());

app.listen(1245, (err) => {
  if (err) {
    console.error("Something bad happened");
  } else {
    console.log("app is listening on port 1245");
  }
});

app.get("/list_products", (req, res) => {
  const listProductsToSend = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));

  res.json(listProductsToSend);
});

const client = createClient();
//utilisation de promisify pour la fonction client.get de Redis
const get = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await get(`item.${itemId}`);
}

app.get("/list_products/:itemId", async (req, res) => {
  try {
    const id = parseInt(req.params.itemId);
    const itemToSend = getItemById(id);
    const currentStock = await getCurrentReservedStockById(id);

    res.json({
      itemId: itemToSend.id,
      itemName: itemToSend.name,
      price: itemToSend.price,
      initialAvailableQuantity: itemToSend.stock,
      currentQuantity: currentStock,
    });
  } catch (err) {
    res.json({ status: "Product not found" });
  }
});

app.get("/reserve_product/:itemId", async (req, res) => {
  try {
    const id = parseInt(req.params.itemId);
    const item = getItemById(id);
    if (!item) {
      res.json({ status: "Product not found" });
      return;
    }
    const currentStock = await getCurrentReservedStockById(id);
    if (currentStock < 1) {
      res.json({ status: "Not enough stock available", itemId: id });
    } else {
      reserveStockById(id, currentStock - 1);
      res.json({ status: "Reservation confirmed", itemId: id });
    }
  } catch (err) {
    res.jsons({ status: "Product not found" });
  }
});

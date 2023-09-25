const express = require("express");
const app = express();
const mysql = require("mysql");

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "moja_baza_danych"
});

app.get("/filtruj", (req, res) => {
  const selectedNosnik = req.query.nosnik;
  const query = `SELECT * FROM plyty WHERE nosnik = ?`;

  db.query(query, [selectedNosnik], (error, results) => {
    if (error) {
      console.error("Błąd zapytania do bazy danych: " + error.message);
      res.status(500).json({ error: "Wystąpił błąd" });
      return;
    }

    res.json(results);
  });
});

app.listen(3000, () => {
  console.log("Serwer nasłuchuje na porcie 3000");
});

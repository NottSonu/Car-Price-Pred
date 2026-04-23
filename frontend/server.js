const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

// Home page (no prediction initially)
app.get("/", (req, res) => {
    res.render("form", { prediction: null });
});

// Handle prediction
app.post("/predict", async (req, res) => {
    try {
        const response = await axios.post("http://127.0.0.1:5000/predict", {
            Present_Price: parseFloat(req.body.present_price),
            Kms_Driven: parseInt(req.body.kms_driven),
            Owner: parseInt(req.body.owner),
            Car_Age: 2025 - parseInt(req.body.year),
            Fuel_Type_Petrol: req.body.fuel === "Petrol" ? 1 : 0,
            Seller_Type_Individual: req.body.seller === "Individual" ? 1 : 0,
            Transmission_Manual: req.body.transmission === "Manual" ? 1 : 0
        });

        // Render result on same page
        res.render("form", {
            prediction: response.data.predicted_price
        });

    } catch (error) {
        res.render("form", {
            prediction: "Error"
        });
    }
});

app.listen(3000, () => {
    console.log("Frontend running on http://localhost:3000");
});
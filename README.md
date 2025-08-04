# Inventory Insights API

![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A backend API built using FastAPI and SQLite to manage inventory data, detect low-stock items, and forecast restocks — with Swagger UI for live testing.

---

##  Features

- Add new inventory items via POST API
- View all inventory records
- Detect low-stock items (quantity < 10)
- Get items restocking within 7 days
- Swagger UI for interactive API testing at `/docs`

---
```
## Project Structure

inventory_api_project/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── db.py # SQLite DB setup
│ ├── models.py # SQLAlchemy models
│ ├── crud.py # Business logic
│ └── routes.py # API endpoints
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```
---

## Sample Request (POST `/inventory/`)

```json
{
  "product_name": "Milk Packet",
  "category": "Grocery",
  "quantity": 6,
  "restock_date": "2025-08-08"
}


```
### How to Run

-Create virtual environment
python -m venv .venv
.venv\Scripts\activate     # Windows

-Install dependencies
pip install -r requirements.txt

-Start the FastAPI server
uvicorn app.main:app --reload
Open in browser:
http://127.0.0.1:8000/docs

---

📈 Use Cases

-Backend for inventory management

-Supply chain and logistics systems

-REST API development and testing

-Data engineering automation projects

---

👩‍💻 Author
Payaswini Rauta
GitHub: [@payaswinirauta](https://github.com/payaswinirauta)

---

📄 License
MIT License

This version is professional, minimal, and **focused only on your project**. Let me know when you're ready for resume line upgrades or deployment setup.








Ask ChatGPT

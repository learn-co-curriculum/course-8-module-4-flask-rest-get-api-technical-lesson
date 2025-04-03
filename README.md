# Technical Lesson: REST & GET APIs with Flask

## Learning Goals

- Understand the purpose of RESTful APIs and HTTP GET methods.
- Build basic Flask routes that respond to GET requests.
- Return structured JSON data from API endpoints.
- Use query parameters to filter responses.
- Follow RESTful conventions in route naming and response structure.

## Introduction

REST (Representational State Transfer) is a widely used architectural style for designing APIs that interact with web resources. The GET method is the foundation for retrieving data in any RESTful service.

In this lesson, we will focus on:

- Building GET routes with Flask.
- Returning mock product data in JSON format.
- Supporting query parameters for filtered responses.
- Following best practices for RESTful design.

Let’s take the example of a product catalog API. This API allows users to:

- View a full list of available products.
- Request a specific product by its ID.
- Filter products by category using a query string.

The current system:

- Uses static mock data to simulate a real backend.
- Needs route handlers that return properly formatted responses.

We will walk through building this GET API step by step and prepare for full CRUD operations in later lessons.

## Code Along

### Setting Up the Project

To get started, clone the repository and install any dependencies.

If you're using `pipenv`:

\`\`\`bash
git clone <repo-url>
cd flask-rest-get-api
pipenv install
\`\`\`

If you're using `pip`:

\`\`\`bash
git clone <repo-url>
cd flask-rest-get-api
pip install -r requirements.txt
\`\`\`

### Writing the GET API with Flask

We’ll define all our routes inside `app.py` and simulate our product catalog with mock data.

#### Example: `app.py`

\`\`\`python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock product data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"})

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
\`\`\`

### Testing the API

Run the app using:

\`\`\`bash
python app.py
\`\`\`

Then visit or test the following endpoints:

- `http://localhost:5000/` – Welcome message  
- `http://localhost:5000/products` – All products  
- `http://localhost:5000/products/2` – Product with ID 2  
- `http://localhost:5000/products?category=books` – Filtered by category  

You can test with your browser, Postman, or curl.

## Best Practices for GET APIs

- Use nouns for resource routes (e.g., `/products` instead of `/getProducts`).
- Always return JSON responses with appropriate HTTP status codes.
- Keep GET requests safe and idempotent—do not modify data.
- Validate and normalize query parameters to prevent case mismatches.
- Follow REST conventions for scalability and readability.

## Conclusion

By building RESTful GET APIs in Flask, developers can:

- Serve consistent, structured data to client applications.  
- Design scalable route structures that follow RESTful standards.  
- Simulate real-world backend functionality before integrating databases.  
- Prepare for more advanced API actions like POST, PATCH, and DELETE.

This lesson sets the foundation for full CRUD development in Flask, allowing you to build interactive and data-driven applications.
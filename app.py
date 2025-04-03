# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: Define mock data for a list of products
# Example: Each product should have id, name, price, and category

# TODO: Implement a homepage route that returns a JSON welcome message

# TODO: Implement GET /products to return all products or filter by category

# TODO: Implement GET /products/<id> to return a single product by ID

if __name__ == "__main__":
    app.run(debug=True)

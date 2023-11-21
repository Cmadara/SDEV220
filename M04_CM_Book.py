from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {"id": 1, "book_name": "The Catcher in the Rye", "author": "J.D. Salinger", "publisher": "Little, Brown and Company"},
    {"id": 2, "book_name": "To Kill a Mockingbird", "author": "Harper Lee", "publisher": "J.B. Lippincott & Co."}
]

# Routes

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "book_name": request.json.get('book_name'),
        "author": request.json.get('author'),
        "publisher": request.json.get('publisher')
    }
    books.append(new_book)
    return jsonify({"message": "Book created successfully", "book": new_book}), 201

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        book['book_name'] = request.json.get('book_name', book['book_name'])
        book['author'] = request.json.get('author', book['author'])
        book['publisher'] = request.json.get('publisher', book['publisher'])
        return jsonify({"message": "Book updated successfully", "book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

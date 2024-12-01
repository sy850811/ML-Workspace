from flask import Flask, request, jsonify

app = Flask(__name__)

to_do_list = [
    {
        "id": 1,
        "name": "ML",
        "description": "Udemy course"
    },
    {
        "id": 2,
        "name": "DSA",
        "description": "IK course"
    }
]

@app.route("/")
def welcome():
    return jsonify({"message": "welcome to this api course"}), 200

@app.route("/items", methods=['GET'])
def get_item():
    return jsonify(to_do_list), 200

@app.route("/items/<int:item_id>", methods=['GET'])
def get_item_by_id(item_id):
    item = next((item for item in to_do_list if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item), 200
    else:
        return jsonify({"Error": f"No item with the id {item_id} found"}), 404

@app.route("/items", methods=['POST'])
def create_item():
    if not request.json or "name" not in request.json or "description" not in request.json:
        return jsonify({"Error": "Invalid Request"}), 400

    new_item = {
        "id": to_do_list[-1]['id'] + 1 if to_do_list else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    to_do_list.append(new_item)
    return jsonify(new_item), 201

@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
    if not request.json or "name" not in request.json or "description" not in request.json:
        return jsonify({"Error": "Invalid Request"}), 400

    item = next((item for item in to_do_list if item['id'] == item_id), None)
    if item is not None:
        item['name'] = request.json.get("name", item["name"])
        item['description'] = request.json.get("description", item["description"])
        return jsonify(item), 200
    else:
        return jsonify({"Error": f"No item with the id {item_id} found"}), 404

@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in to_do_list if item['id'] == item_id), None)
    if item:
        to_do_list.remove(item)
        return jsonify({"result": "Item deleted"}), 200
    else:
        return jsonify({"Error": f"No item with the id {item_id} found"}), 404

if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Helper function to find an event by ID
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # TODO: Task 2 - Design and Develop the Code

    # check that the title is provided in the request data
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
 

    # TODO: Task 3 - Implement the Loop and Process Each Element

    #  Generate a new ID for the event
    new_id = max([event.id for event in events], default=0) + 1
    # Create a new event instance
    new_event = Event(new_id, data["title"])

    # Add the event to the in-memory list
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    
    # find the event
    event = find_event(event_id)
    if event is None:
       return jsonify({"error": "Event not found"}), 404 

    # Get the JSON data from the request
    data = request.get_json()

    #Check that the title is provided in the request data
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    # TODO: Task 3 - Implement the Loop and Process Each Element
     
     # Update the event's title
    event.title = data["title"]
    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # Find the event by ID
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # Remove the event from the list
    events.remove(event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify({"message": "Event deleted successfully"}), 200
if __name__ == "__main__":
    app.run(debug=True)

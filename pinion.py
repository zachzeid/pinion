from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def onboard_user(user_info, systems):
    # Logic to onboard the user to specified systems
    # Placeholder - replace with actual logic
    print(f"Onboarding {user_info} to systems: {systems}")

def offboard_user(user_info):
    # Logic to offboard the user from all systems
    # Placeholder - replace with actual logic
    print(f"Offboarding {user_info}")

@app.route('/onboard', methods=['POST'])
def onboard():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    scheduled_date = data.get('scheduled_date')
    systems = data.get('systems', [])
    
    # Convert scheduled_date to datetime object
    try:
        scheduled_date = datetime.strptime(scheduled_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'scheduled_date': scheduled_date
    }
    
    onboard_user(user_info, systems)
    return jsonify({'message': 'Onboarding scheduled successfully'}), 200

@app.route('/offboard', methods=['POST'])
def offboard():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    scheduled_date = data.get('scheduled_date')

    # Convert scheduled_date to datetime object
    try:
        scheduled_date = datetime.strptime(scheduled_date, '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'scheduled_date': scheduled_date
    }

    offboard_user(user_info)
    return jsonify({'message': 'Offboarding scheduled successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

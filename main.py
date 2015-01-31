from flask import Flask, request
app = Flask(__name__)

@app.route('/announce', methods=['GET'])
def root():
    info_hash = request.args.get('info_hash')
    peer_id = request.args.get('peer_id')
    port = request.args.get('port')
    uploaded = request.args.get('uploaded')
    downloaded = request.args.get('downloaded')
    left = request.args.get('left')
    compact = request.args.get('compact')
    no_peer_id = request.args.get('no_peer_id')
    event = request.args.get('event')
    ip = request.args.get('ip')
    numwant = request.args.get('numwant')
    key = request.args.get('key')
    trackerid = request.args.get('trackerid')

    


if __name__ == '__main__':
    app.run(debug = True)
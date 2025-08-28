from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', api_key='AIzaSyAAaBbOLTG04ZZdNzjiUCqHw_YDB1FOmlY')

@app.route('/trial_inter')
def trial_inter():
    return render_template('trial_inter.html', api_key='AIzaSyAAaBbOLTG04ZZdNzjiUCqHw_YDB1FOmlY')

@app.route('/trial_inter/ajax', methods=['POST'])
def trial_inter_ajax():
    data = request.get_json()
    print(data['address'])
    return jsonify(success=True)

@app.route('/trial_2')
def trial_2():
    return render_template('trial_2.html', api_key='AIzaSyAAaBbOLTG04ZZdNzjiUCqHw_YDB1FOmlY')

@app.route('/iso_trial')
def iso_trial():
    return render_template('iso_trial.html',api_key='AIzaSyAAaBbOLTG04ZZdNzjiUCqHw_YDB1FOmlY')


@app.route('/log_error', methods=['POST'])
def log_error():
    data = request.get_json()
    error_message = data.get('error', None)

    if error_message:
        print("JavaScript Error:", error_message)
        return jsonify(success=True, message="Error logged.")
    else:
        return jsonify(success=False, message="No error provided."), 400

if __name__ == '__main__':
    app.run()

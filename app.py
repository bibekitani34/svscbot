# Author: Bibek Itani
# Date: 11/08/21

from flask import Flask, render_template, request
import chatbot as inp
from datetime import datetime


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return render_template("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    now = datetime.now()
    question_time = now.strftime("%H:%M:%S")
    # console
    print("question time:", question_time)
    print(request.form)
    ##endsconsole
    question = request.form["question"]
    response = inp.chat(question)
    now = datetime.now()
    answer_time = now.strftime("%H:%M:%S")
    print("answer time:", answer_time)
    print(response)
    return """
        <div class="outgoing_msg">
            <div class="sent_msg">
                <p>%s</p>
                <span class="time_date time"> You   |    %s</span> </div>
            </div>
        </div>
        <div class="incoming_msg">
            <div class="incoming_msg_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil"> </div>
            <div class="received_msg">
                <div class="received_withd_msg">
                    <p>%s</p>
                    <span class="time_date">Virtual Assistant |  %s</span></div>
            </div>
        </div>
    """ % (
        question,
        question_time,
        response,
        answer_time,
    )


if __name__ == "__main__":
    app.run(port = 5003, debug=True)
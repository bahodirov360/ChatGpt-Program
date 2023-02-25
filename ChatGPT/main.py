from flask import *
import webview
import openai
from pytarjimon import tarjima

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def tug():
    return render_template("button.html")


@app.route('/eng', methods=['GET', 'POST'])
def sura():
    openai.api_key = "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"

    if request.method == 'POST':
        prompt = request.form['sura']
        if prompt == "What is your name?" or prompt == "what is your name?" or prompt == "What is your name" or prompt == "what is your name":
            ism = "My name is Magic Chat"
            return render_template('input.html', ism = ism)
        if prompt == "How old are you?" or prompt == "how old are you?" or prompt == "How old are you" or prompt == "how old are you":
            yosh = "As an artificial intelligence language model, I do not have an age like humans do. I was created by Nodir and my knowledge is constantly updated, so I always provide the most up-to-date information."
            return render_template('input.html', yosh=yosh)
        else:
            response = openai.Completion.create(
                engine="text-davinci-003", prompt=prompt, max_tokens=1024)
            javob = response["choices"][0]["text"]
    
            return render_template('input.html', javob=javob)
    else:
        return render_template('input.html')


@app.route('/uz', methods=['GET', 'POST'])
def surama():
    openai.api_key = "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"

    if request.method == 'POST':
        rere = request.form['surama']
        tr = tarjima(rere, "en")
        responsese = openai.Completion.create(
            engine="text-davinci-003", prompt=tr, max_tokens=1024)
        javobi = responsese["choices"][0]["text"]
        tr2 = tarjima(javobi, "uz")
    
        return render_template('uz.html', tr2=tr2)
    else:
        return render_template('uz.html')


@app.route('/rus', methods=['GET', 'POST'])
def surammama():
    openai.api_key = "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"

    if request.method == 'POST':
        rebe = request.form['suraaama']
        tarr = tarjima(rebe, "en")
        responsese = openai.Completion.create(
            engine="text-davinci-003", prompt=tarr, max_tokens=1024)
        javobi = responsese["choices"][0]["text"]
        tr3 = tarjima(javobi, "ru")
    
        return render_template('rus.html', tr3=tr3)
    else:
        return render_template('rus.html')

# app.run(debug=True)
webview.create_window('ChatGPT', app, min_size=(700, 600))
webview.start(gui="qt")

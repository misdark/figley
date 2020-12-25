from flask import Flask, render_template, request
import figlet
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    output = ""
    fz = ""
    if request.method == 'POST':
        text = request.form['text']
        try:
            fz = 70/len(text)
        except:
            if ZeroDivisionError:
                pass
        topping = request.form['topping']
        output = figlet.let(text, topping)
        return render_template('index.html', output=output, fz=fz)
        
    return render_template('index.html', output=output, fz=fz)

if __name__ == '__main__':
    app.run(debug=True)

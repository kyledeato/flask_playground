from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def change_color(color="blue",num=3):
    return render_template("index.html", background_color = color,num = num)

if __name__=="__main__":
    app.run(debug=True)
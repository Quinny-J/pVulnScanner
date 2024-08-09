from flask import Flask, render_template, request
import xss_checker
import sql_injection_checker

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website = request.form['website']
        xss_results = xss_checker.check_xss(website)
        sql_results = sql_injection_checker.check_sql_injection(website)
        return render_template('index.html', xss_results=xss_results, sql_results=sql_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

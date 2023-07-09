from flask import Flask, render_template, request
from text_summary import summarizer


app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods= ['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        inputData= request.form['inputParagraph']
        summary, orginal_txt, len_org_txt, len_summary_txt= summarizer(inputData)

    return render_template('summary.html', summary= summary, orginal_txt= orginal_txt, len_org_txt= len_org_txt, len_summary_txt= len_summary_txt)        




if __name__ == "__main__":
    app.run(debug=True)



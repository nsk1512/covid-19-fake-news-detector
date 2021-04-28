#Importing the Libraries
import flask
from flask import Flask, request,render_template
from flask_cors import CORS
import os
import pickle
import newspaper
from newspaper import Article
import urllib
import nltk
#import COVID19Py
#covid19 = COVID19Py.COVID19()
#data = covid19.getLatest()


#Loading Flask and assigning the model variable
app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

# Loading the model
with open('model.pickle', 'rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    return render_template('main.html')

#Receiving the input text from the user
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        keywords= ['coronavirus','covid','covid19','virus','vaccine','sarscov2','COVID','COVID19','COVID-19',
        'SARS-CoV-2','quarantine','lockdown','viruses','coronaviruses','pandemic','Covid',
        'curfew','Curfew','oxygen','Oxygen', 'remdesivir','ventilator','deaths','covaxin',
        'covishield','mutant','mutation']
        url = request.get_data(as_text=True)[8:]
        url = urllib.parse.unquote(url)
        try:
            if(url.startswith('http://') or url.startswith('https://')):
                print(url)
                article=Article(str(url),language="en")
                article.download()
                article.parse()
                #nltk.download('punkt')
                article.nlp()
                a = article.title
                title=""
                count=0
                for i in a:
                    if(i.isspace()):
                        count=count+1
                    if count==9:
                        break
                    else:
                        title+=i
                print(title)
                b = article.keywords
                print(b)
                c = article.authors
                print(c)
                summary=article.summary
                if any(x in b for x in keywords):
                    print(summary)
                    # Predicting the input
                    pred = model.predict([summary])
                    return render_template('pred.html', prediction_text='This article is {}.'.format(pred[0]), title=title,author=c,leno=len(c),active=1, keywords=b,summary=summary, lenk=len(keywords))
                else:
                    print("news unrelated")
                    return render_template('pred.html', message='This article is unrelated to Covid 19. No results obtained.', active=1)

            elif(len(url) > 25):
                print(url)
                if any(x in url for x in keywords):
                    pred = model.predict([url])
                    return render_template('pred.html', prediction_text='This news is {}.'.format(pred[0]), active=1)
                else:
                    return render_template('pred.html', message='This article is unrelated to Covid 19. No results obtained.', active=1)

            else:
                return render_template('pred.html', message='Data is insufficient. Min. length is 25 characters.', active=1)

        except:
            print("Invalid")
            return render_template('pred.html', text='Invalid Url. Please enter an existing URL.', active=1)
    return render_template('pred.html')


    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
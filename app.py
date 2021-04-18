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
import COVID19Py
covid19 = COVID19Py.COVID19()
data = covid19.getLatest()


#Loading Flask and assigning the model variable
app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

# Loading the model
with open('logistic.pickle', 'rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    percentConf=(data['confirmed']/(data['confirmed']+data['recovered']+data['deaths']))*100
    print(percentConf)
    return render_template('main.html', data=data,percentConf=percentConf)

#Receiving the input text from the user
@app.route('/',methods=['GET','POST'])
def predict():
    if(request.form.get('action')=='check'):
        keywords= ['coronavirus','covid','covid19','virus','vaccine','sarscov2','COVID','COVID19','COVID-19','SARS-CoV-2','quarantine','lockdown','viruses','coronaviruses','pandemic','Covid']
        url = request.form['message']
        url = urllib.parse.unquote(url)
        try:
            if(url.startswith('http://') or url.startswith('https://')):
                print(url)
                article=Article(str(url),language="en")
                article.download()
                article.parse()
                nltk.download('punkt')
                article.nlp()
                a = article.title
                print(a)
                b = article.keywords
                print(b)
                c = article.authors
                print(c)
                summary=article.summary
                if any(x in summary for x in keywords):
                    print(summary)
        # Predicting the input
                    pred = model.predict([summary])
                    return render_template('main.html', prediction_text='This article is {}.'.format(pred[0]), active=1, data=data)
                else:
                    print("news unrelated")
                    return render_template('main.html', message='This article is unrelated to Covid 19. No results obtained.', active=1,data=data)
            elif(len(url) > 25):
                print(url)
                if any(x in url for x in keywords):
                    pred = model.predict([url])
                    return render_template('main.html', prediction_text='This news is {}.'.format(pred[0]), active=1,data=data)
                else:
                    return render_template('main.html', message='This article is unrelated to Covid 19. No results obtained.', active=1,data=data)

            else:
                return render_template('main.html', message='Data is insufficient. Min. length is 25 characters.', active=1,data=data)

        except:
            print("Invalid")
            return render_template('main.html', text='Invalid Url. Please enter an existing URL.', active=1,data=data)

    elif(request.form.get('action')=='show'):
        keywords= ['coronavirus','covid','covid19','virus','vaccine','sarscov2','COVID','COVID19','COVID-19','SARS-CoV-2','quarantine','lockdown','viruses','coronaviruses','pandemic','Covid']
        url = request.form['message']
        url = urllib.parse.unquote(url)
        try:
            if(url.startswith('http://') or url.startswith('https://')):
                print(url)
                article=Article(str(url),language="en")
                article.download()
                article.parse()
                nltk.download('punkt')
                article.nlp()
                a = article.title
                print(a)
                b = article.keywords
                print(b)
                c = article.authors
                print(c)
                summary=article.summary
                if any(x in summary for x in keywords):
                    print(summary)
        # Predicting the input
                    pred = model.predict([summary])
                    return render_template('main.html', prediction_text='This article is {}.'.format(pred[0]), title=a,author=c,leno=len(c), active=1, keywords=b, lenk=len(keywords),data=data)
                else:
                    print("news unrelated")
                    return render_template('main.html', message='This article is unrelated to Covid 19. No results obtained.', active=1, keywords=b, lenk=len(keywords),data=data)
            elif(len(url) > 25):
                print(url)
                if any(x in url for x in keywords):
                    pred = model.predict([url])
                    return render_template('main.html', prediction_text='This news is {}.'.format(pred[0]), title=a,author=c,leno=len(c), active=1, keywords=b, lenk=len(keywords),data=data)
                else:
                    return render_template('main.html', message='This article is unrelated to Covid 19. No results obtained.', active=1, keywords=b, lenk=len(keywords),data=data)

            else:
                return render_template('main.html', message='Data is insufficient. Min. length is 25 characters.', active=1, keywords=b, lenk=len(keywords),data=data)

        except:
            print("Invalid")
            return render_template('main.html', text='Invalid Url. Please enter an existing URL.', active=1, keywords=b, lenk=len(keywords),data=data)


    

    
    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
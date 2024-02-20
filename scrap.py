from flask import Flask, render_template, request,redirect, url_for,session
import random
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup



app = Flask(__name__)
ua = UserAgent()

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/scrapcontent',methods=['POST'])
def scrapcontent():
    scrapurl = request.form['scrapurl']
    url = scrapurl
    user_agent = ua.random
    headers = {
    'User-Agent': user_agent
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    h3_tags = soup.find_all('h1')
    result=''
    if len(h3_tags) == 0:
        result = response.content
    else:
        for tag in h3_tags:
            result= tag.text
    return render_template('index.html',result=result)





if __name__ == '__main__':
    app.run(debug=True)


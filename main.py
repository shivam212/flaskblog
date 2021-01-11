from flask import Flask, send_file
from flask import render_template
from connect import links, myquery, random_post
app = Flask(__name__)

@app.route('/')
def index():
        link = links()
        if len(link) > 5:
                link = link[:5]
        posts = [[x['title'],x['post_data'],x['redirect']] for x in link]
        return render_template('layout.html',posts = posts)
@app.route('/aboutme')
def aboutme():
        return render_template('about.html')
@app.route('/archive')
def archive():
        link = links()
        titles = [[x['title'],x['redirect']] for x in link]
        return render_template('archive.html', titles=titles)
@app.route('/blogpost/<pId>')
def blogpost(pId):
        post = myquery(pId)
        post_data = post[0]['post_data']
        title = post[0]['title']
        date = post[0]['date']
        randompid = random_post()
        randomPostTitle = myquery((randompid))[0]['title']
        return render_template('post.html', title=title, post_data=post_data, date = date, randompid = randompid, randomPostTitle = randomPostTitle)
@app.route('/resume')
def show_static_pdf():
    with open('static/data/resume.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='resume.pdf')
if __name__=="__main__":
        app.run()

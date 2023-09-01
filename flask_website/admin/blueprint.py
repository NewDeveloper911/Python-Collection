from flask import Flask, Blueprint, redirect, url_for, render_template,request, session, flash, current_app, g
from databases import db, Learning, Tag, users, Replies #This allows me to access databases in other files
import datetime

blueprint = Blueprint("blueprint",  __name__, static_folder="static", template_folder="templates")
'''
Here, I have just told my program of the locations of my static (unchanging files) and template (html webpages) folders
'''
upvote = 1
downvote = 1

@blueprint.route("/home")
@blueprint.route("/") 
def home():
    Posts = Learning.query.limit(5) # Fetches all todos from my database
    return render_template("flaskindex.html", posts=Posts, user=users.query.filter_by(name=g.user).first())

@blueprint.route("/contribute", methods=['POST','GET'])
def contribute():
    if request.method == 'POST':
        title=request.form.get('title')
        body=request.form.get('body')
        if not title or len(title) < 12:
            flash("Please ensure that you have entered a question of a reasonable length", category='warning')
        elif not body or len(body) < 12:
            flash("Please ensure that you have entered enough details about your question (subject, sub-topic etc) of a reasonable length", category='warning')
        else:
            new_post = Learning(title=title, body=body, timestamp=datetime.datetime.now(),question_author=users.query.filter_by(name=session.get('user')).first())
            db.session.add(new_post)
            db.session.commit()
            flash("Post submitted successfully", category='message')

        tags=request.form.get('tags').split(', ')
        for i in tags:
            new_tag = Tag(name=i)
            db.session.add(new_tag)
            db.session.commit()

    #Save until I actually implement upvotes and downvotes
    #return render_template("flaskindex.html", detail=str(session.get('user')), user=users.query.filter_by(name=session.get('user')).first(), posts=Learning.query.filter(Learning.upvotes>Learning.downvotes).order_by(Learning.upvotes-Learning.downvotes).limit(10))
    return render_template("flaskindex.html", detail=str(session.get('user')), user=users.query.filter_by(name=session.get('user')).first(), posts=Learning.query.limit(10))

@blueprint.route("/answer/<int:id>", methods=['POST','GET'])
def answer(id):
    post = Learning.query.filter_by(id=id).first()
    if request.method == 'POST':
        body=request.form.get('reply_text')
        if not body or len(body) < 12:
            flash("Please ensure that you have entered enough details about your answer of a reasonable length", category='warning')
        else:
            answer = Replies(reply=body,comment_author=users.query.filter_by(name=session.get('user')).first(),post=post)
            db.session.add(answer)
            db.session.commit()
            flash("Answer submitted successfully", category='message')

    return render_template("flaskindex.html", detail=str(session.get('user')), user=users.query.filter_by(name=session.get('user')).first(), posts=Learning.query.limit(10))

@blueprint.route("/edit_post/<int:id>", methods=['POST','GET'])
def edit_post(detail):
    if request.method == "POST":
        post = Learning.query.filter_by(id=id).first()
        title = request.form.get("title")
        if title:
            post.title = title
            flash("Question has been saved successfully")
            current_app.logger.info("Your question, which is " + str(post.query.filter_by(title=title).first().title) + " has been saved successfully")

        body = request.form.get('body')
        if body:
            post.body = body
            flash("Question body has been saved successfully")
            current_app.logger.info("Your question details, which is " + str(post.query.filter_by(body=body).first().body) + " has been saved successfully")

        tags = request.form.get('tags').split(', ')
        if tags:
            post.tags = tags
            db.session.add(post)
            flash("New tags have been saved successfully")
            current_app.logger.info("Your tags, which is " + str(post.query.filter_by(tags=tags).first().tags) + " has been saved successfully")

        post.last_modified = datetime.datetime.now()

        db.session.commit()
        
        return render_template("flaskindex.html", detail=str(detail), user=users.query.filter_by(name=detail).first(), posts=Learning.query.filter(db.Learning.upvotes>db.Learning.downvotes).order_by(db.Learning.upvotes-db.Learning.downvotes).limit(10))
    else:
        if detail:
            return render_template("flaskindex.html", detail=str(detail), user=users.query.filter_by(name=detail).first(), posts=Learning.query.filter(db.Learning.upvotes>db.Learning.downvotes).order_by(db.Learning.upvotes-db.Learning.downvotes).limit(10))
        else:
            current_app.logger.info("Tried to skip the queue, huh? Your mistake.")
            flash("You are not logged in yet, you should login in for full access to all features")
            return redirect(url_for("login"))

@blueprint.route('/upvote/<id>')
def upvote(id):
    #return "<h1>{}</h1>".format(id)
    item = Learning.query.filter_by(id=int(id)).first()
    if session.get('user') == item.question_author:
        upvote = -upvote
        item.upvotes += upvote
    db.session.commit()
    return redirect(url_for("blueprint.home"))

@blueprint.route('/downvote/<id>')
def downvote(id):
    #return "<h1>{}</h1>".format(id)
    item = Learning.query.filter_by(id=int(id)).first()
    if session.get('user') == item.question_author:
        downvote = -downvote
        item.upvotes -= downvote
    db.session.commit()
    return redirect(url_for("blueprint.home"))

@blueprint.route('/upvote_post/<id>')
def post_upvote(id):
    #return "<h1>{}</h1>".format(id)
    item = Replies.query.filter_by(id=int(id)).first()
    item.upvotes +=1
    db.session.commit()
    return redirect(url_for("blueprint.home"))

@blueprint.route('/downvote_post/<id>')
def post_downvote(id):
    #return "<h1>{}</h1>".format(id)
    item = Replies.query.filter_by(id=int(id)).first()
    item.downvotes +=1
    db.session.commit()
    return redirect(url_for("blueprint.home"))

@blueprint.route("/pomodoro", methods=['GET','POST'])
def pomodoro():
    return render_template("pomodoro.html", detail=str(session['user']), user=users.query.filter_by(name=session['user']).first())
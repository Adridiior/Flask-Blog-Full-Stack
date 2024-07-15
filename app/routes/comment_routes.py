from flask import Blueprint, url_for, flash, redirect, request, abort
from app import db
from app.forms import CommentForm
from app.models import Comment, Post
from flask_login import current_user, login_required

comment = Blueprint('comment', __name__)

@comment.route("/post/<int:post_id>/comment", methods=['POST'])
@login_required
def comment_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, user_id=current_user.id, post_id=post.id)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    return redirect(url_for('post.post', post_id=post.id))

@comment.route("/comment/<int:comment_id>/delete", methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if comment.author != current_user:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!', 'success')
    return redirect(url_for('post.post', post_id=comment.post_id))

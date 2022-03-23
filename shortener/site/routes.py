from flask import Blueprint, render_template, request, redirect, url_for
from shortener.forms import URLInputForm
from shortener.models import db, Link

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/', methods=['GET','POST'])
def home():
    form = URLInputForm()
    if request.method == 'POST' and form.validate_on_submit():
        link = form.link.data
        print(link)
        check = Link.query.filter_by(link=link)
        if check.first():
            return render_template('home.html', form = form, created_link = f'{request.base_url}'+ check.first().id, already = True)
        new_link = Link(link)
        db.session.add(new_link)
        db.session.commit()
        return render_template('home.html', form = form, created_link = f'{request.base_url}'+ new_link.id)

    return render_template('home.html', form = form)

@site.route('/<link_id>')
def go_to_link(link_id):
    try:
        record = Link.query.get(link_id)
        web_address = record.link
        return redirect(web_address)
    except:
        return f'This is not a valid shortURL! Please revisit {request.base_url.strip(link_id)} to create it!'
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def total():
    return render_template('base.html')

@app.route('/clotching/')
def cloth():
    garments=[
        {'name':'Футболка', 'price':'52', 'size':'M', 'img':'../static/img/clothing1.jpg'},
        {'name':'Свитшот', 'price':'125', 'size':'XL','img':'../static/img/clothing2.jpg'},
        {'name':'Платье', 'price':'82', 'size':'M','img':'../static/img/clothing3.jpg'}
    ]
    return render_template('cloth.html', garments=garments)

@app.route('/footwear/')
def footer():
    shoe=[
        {'name':'Кроссовки', 'price':'1025', 'size':'38','img':'../static/img/footwear1.jpg'},
        {'name':'Ботильоны', 'price':'978', 'size':'39','img':'../static/img/footwear2.jpg'},
        {'name':'Кроссовки', 'price':'877', 'size':'36','img':'../static/img/footwear3.jpg'}
    ]
    return render_template('footwear.html', shoe=shoe)

if __name__ == '__main__':
    app.run(debug=True)
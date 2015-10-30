from flask import Flask, render_template, request
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html', title='Hello!')

@app.route('/more/')
def more():
    return render_template('index.html')

# @app.route('/')
# def submission_page():
#     return '''
#         <form action="/map" method='POST' >
#             <input type="text" name="user_input" />
#             <input type="submit" />
#         </form>
#         '''


# My word counter app
@app.route('/map', methods=['POST'] )
def map():
    text = str(request.form['user_input'])

    map_dict={'Food On The Stove':"https://clowen.cartodb.com/viz/4bda1c9e-5bfa-11e5-b50f-0e9d821ea90d/embed_map",
'all fire torque':"https://clowen.cartodb.com/viz/b7b00480-5b44-11e5-a399-0e8dde98a187/embed_map",
'Illegal Burn':"https://clowen.cartodb.com/viz/c8597922-5bff-11e5-8edf-0e9d821ea90d/embed_map",
'Monorail Fire on the beam':"https://clowen.cartodb.com/viz/0e0403e4-5bff-11e5-97cc-0e853d047bba/embed_map",
'Dumpster Fire':"https://clowen.cartodb.com/viz/3aa5156e-5bff-11e5-956e-0e73ffd62169/embed_map",
'Rubbish Fire':"https://clowen.cartodb.com/viz/5dc4a924-5bff-11e5-a999-0ec6f7c8b2b9/embed_map",
'Rescue Lock In/Out':"https://clowen.cartodb.com/viz/339fb4bc-5c00-11e5-9e28-0e73ffd62169/embed_map",
'Shed Fire':"https://clowen.cartodb.com/viz/7c0240cc-5bff-11e5-90a7-0e018d66dc29/embed_map",
'Garage Fire':"https://clowen.cartodb.com/viz/9115472a-5bff-11e5-9641-0e0c41326911/embed_map",
'Chimney Fire':"https://clowen.cartodb.com/viz/a466d30c-5bff-11e5-a58e-0e9d821ea90d/embed_map",
'Brush Fire':"https://clowen.cartodb.com/viz/b82381ba-5bff-11e5-94c4-0e9d821ea90d/embed_map",
'Pier Fire':"https://clowen.cartodb.com/viz/e09308c8-5bff-11e5-9641-0e0c41326911/embed_map",
'Tunnel Fire':"https://clowen.cartodb.com/viz/fdc91e3c-5bff-11e5-97cc-0e853d047bba/embed_map",
'Transformer Fire':"https://clowen.cartodb.com/viz/13e6f5a4-5c00-11e5-a6f1-0e018d66dc29/embed_map"}


    if 'food' in text.lower():
        key = 'Food On The Stove'
    elif 'burn' in text.lower():
        key = 'Illegal Burn'
    elif 'monorail' in text.lower():
        key = 'Monorail Fire on the beam'
    elif 'dumpster' in text.lower():
        key = 'Dumpster Fire'
    elif 'rubbish' in text.lower():
        key = 'Rubbish Fire'
    elif 'lock' in text.lower():
        key = 'Rescue Lock In/Out'
    elif 'shed' in text.lower():
        key = 'Shed Fire'
    elif 'garage' in text.lower():
        key = 'Garage Fire'
    elif 'chimney' in text.lower():
        key = 'Chimney Fire'
    elif 'brush' in text.lower():
        key = 'Brush Fire'
    elif 'pier' in text.lower():
        key = 'Pier Fire'
    elif 'tunnel' in text.lower():
        key = 'Tunnel Fire'
    elif 'transformer' in text.lower():
        key = 'Transformer Fire'

    else:
        key = 'Rescue Lock In/Out'
        maplink = map_dict[key]
        return render_template('locked_out.html', map_name = 'Rescue Lock In/Out', maplink = maplink)
    maplink = map_dict[key]
    map_name = key



    return render_template('map.html', map_name = map_name, maplink = maplink)
    # word_counts = Counter(text.lower().split())
    # page = 'There are {0} words.<br><br>Individual word counts:<br> {1}'
    # return page.format(len(word_counts), dict_to_html(word_counts))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

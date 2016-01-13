from flask import Flask, render_template, request
import mapDict
app = Flask(__name__)


# home page
@app.route('/')
def index():
    return render_template('index.html', title='Hello!')


@app.route('/more/')
def more():
    return render_template('index.html')


# My word counter app
@app.route('/map', methods=['POST'])
def map():
    text = str(request.form['user_input'])

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
        return render_template('locked_out.html',
                               map_name='Rescue Lock In/Out', maplink=maplink)
    maplink = map_dict[key]
    map_name = key

    return render_template('map.html', map_name=map_name, maplink=maplink)
    # word_counts = Counter(text.lower().split())
    # page = 'There are {0} words.<br><br>Individual word counts:<br> {1}'
    # return page.format(len(word_counts), dict_to_html(word_counts))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

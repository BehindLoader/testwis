from server import server, models, utils
from flask import render_template, send_file, jsonify, request
from os import path
from datetime import datetime

STATIC_FOLDER = str( path.abspath('./src') )

@server.route('/')
def index_view():
    return render_template('index.html')

@server.route('/src/<path:filename>')
def src(filename):
    return send_file( path.join(STATIC_FOLDER, filename) )

@server.route('/api/rate')
def rate():
    """ Возвращает курс валюты на текущее число """
    value = request.args.get('value')
    if value:
        value = value.upper()
    else:
        return jsonify(dict(
            status = 'error',
            message = 'Необходимо ввести название валюты'
        )), 400
    query = models.Value.select().where(
        models.Value.name == value,
        models.Value.date == datetime.now()
    )
    if not query.count(): # если такой записи нет, то получаем ее
        valute = utils.get_valute(value)
        if not valute:
            return jsonify(dict(
                status = 'error',
                message = 'Нет информации о такой валюте'
            )), 404
        models.Value(
            name = value,
            value = valute['Value'],
            date = datetime.now()
        ).save()
        query = models.Value.select().where(
            models.Value.name == value,
            models.Value.date == datetime.now()
        )
    response = dict(
        status = 'ok',
        result = dict(
            name = query.get().name,
            value = query.get().value,
        )
    )
    return jsonify(response)

@server.route('/api/convert')
def convert():
    """ Конвертирует валлюту """
    name = request.args.get('name').upper()
    try:
        value = float(request.args.get('value'))
    except:
        return jsonify(dict(
            status = 'error',
            message = 'Значение должно быть числом'
        )), 400
    if not name or not value:
        return jsonify(dict(
            status = 'error',
            message = 'Необходимо ввести название и значение валюты'
        )), 400
    query = models.Value.select().where(
        models.Value.name == name,
        models.Value.date == datetime.now()
    )
    if not query.count(): # если такой записи нет, то получаем ее
        valute = utils.get_valute(name)
        models.Value(
            name = name,
            value = valute['Value'],
            date = datetime.now()
        ).save()
        query = models.Value.select().where(
            models.Value.name == name,
            models.Value.date == datetime.now()
        )
    result = value * query.get().value
    response = dict(
        status = 'ok',
        value = result,
        name = name
    )
    return jsonify(response)
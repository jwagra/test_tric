"""test_tric"""
from datetime import datetime, time

from flask import request, jsonify, Response

from sqlalchemy import text

from test_tric import APP, DB
from test_tric.models import State


DATE_FORMAT = '%Y-%m-%d'


@APP.route('/state/<service_name>', methods = ('GET', 'POST'))
def state(service_name):
    """test_tric"""
    if request.method == 'GET':
        service_states = State.query.filter_by(service_name=service_name).order_by(State.state_datetime.desc())
        return jsonify([s_s.to_dict() for s_s in service_states])

    if request.method == 'POST':
        data = request.form
        _state = State(
            service_name=data['service_name'],
            state_type=data['state_type'],
            state_datetime=data.get('state_datetime') or datetime.now(),
            info=data.get('info'),
        )
        DB.session.add(_state)
        DB.session.commit()
        return jsonify({'id': _state.id})

    return Response('incompatible method', status=400)


@APP.route('/states', methods = ('GET', ))
def states():
    """test_tric"""
    try:
        on_date = request.args.get('on_date')
        if on_date:
            on_date = datetime.strptime(on_date, DATE_FORMAT).date()
        else:
            on_date = datetime.today()
    except ValueError:
        return Response(f'acceptable date format: {DATE_FORMAT}', status=400)

    with DB.engine.connect() as connection:
        sql = f"""
            WITH prepared AS (
                SELECT
                    service_name
                    , state_type
                    , state_datetime
                    , row_number() OVER (PARTITION BY service_name ORDER BY state_datetime DESC) AS rn
                FROM {State.__table__.name}
                WHERE
                    state_datetime BETWEEN :datetime_start AND :datetime_end
            )
            SELECT
                service_name
                , state_type
                , state_datetime
            FROM prepared
            WHERE
                rn = 1
        """
        service_states = connection.execute(
            text(sql),
            {
                'datetime_start': datetime.combine(on_date, time(0, 0, 0)),
                'datetime_end': datetime.combine(on_date, time(23, 59, 59)),
            }
        )
        result = []
        for s_s in service_states:
            result.append({
                'service_name': s_s.service_name,
                'state_type': s_s.state_type,
                'state_datetime': str(s_s.state_datetime),
            })
        return jsonify(result)

if __name__ == '__main__':
    APP.run()

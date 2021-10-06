import sqlalchemy
from app.exc.TasksError import ImportanceAndUrgencyError
from app.models.categorie_model import Categorie
from app.models.eisenhower_model import Eisenhower
from app.models.task_model import Task
from flask import current_app, request

from dataclasses import asdict

import pdb

def create() -> dict:
    data = request.get_json()
    importance, urgency = data['importance'], data['urgency']
    try:

        if importance_and_urgency_is_valid(importance, urgency) is False:
            raise ImportanceAndUrgencyError(importance, urgency)

        eisenhower = correct_type_eisenhower(importance, urgency)

        data['eisenhower_id'] = eisenhower.id
        data['eisenhower_classification'] = eisenhower

        data = get_and_create_category(data)
        data.pop('categories')

        add_task = Task(**data)
        session = current_app.db.session
        session.add(add_task)
        session.commit()

        task = asdict(add_task)
        task['category'] = add_task.category
        task['eisenhower_classification'] = eisenhower.type

        return task
    except ImportanceAndUrgencyError as err:

        return err.message, 404
    except sqlalchemy.exc.IntegrityError:
        return {'msg': "Task already exists"}, 409


def update(id: int):
    eisenhower = ''
    data = request.get_json()
    get_task = Task.query.get(id)

    try:

        if 'importance' in data:
            importance = data['importance']
            eisenhower = correct_type_eisenhower(importance, get_task.urgency)
            data['eisenhower_classification'] = eisenhower

        if 'urgency' in data:
            importance = data['urgency']
            eisenhower = correct_type_eisenhower(get_task.importance, urgency)
            data['eisenhower_classification'] = eisenhower

        data['eisenhower_id'] = eisenhower.id

        for key, value in data.items():
            setattr(get_task, key, value)

        current_app.db.session.commit()
        task = Task.query.get(id)

        return {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "duration": task.duration,
            "eisenhower_classification": task.eisenhower_classification.type,
                }, 200
    except AttributeError:
        return {'msg': 'task not found!'}, 404


def delete(id: int):
    try:
        query = Task.query.get(id)
        current_app.db.session.delete(query)
        current_app.db.session.commit()

        return '', 204
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        return {'msg': 'task not found!'}, 404


def correct_type_eisenhower(importance: int, urgency: int):

    if importance is 1 and urgency is 1:
        data_type = Eisenhower.query.filter_by(type='Do It First').first()
        return data_type

    if importance is 1 and urgency is 2:
        data_type = Eisenhower.query.filter_by(type='Delegate It').first()
        return data_type

    if importance is 2 and urgency is 1:
        data_type = Eisenhower.query.filter_by(type='Schedule It').first()
        return data_type

    return Eisenhower.query.filter_by(type='Delete It').first()


def get_and_create_category(data):
    category_list = []
    for item in data['categories']:

        category = Categorie.query.filter_by(name=item['name']).first()

        if category is not None:
            category_list.append(category)
            data['category'] = category_list

        if category is None:
            add_category = Categorie(name=item['name'])
            session = current_app.db.session
            session.add(add_category)
            session.commit()

            category_list.append(add_category)

            data['category'] = category_list

    return data


def importance_and_urgency_is_valid(importance, urgency) -> bool:
    if importance <= 0 or importance > 2:
        return False

    if urgency <= 0 or urgency > 2:
        return False

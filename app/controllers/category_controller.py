from dataclasses import asdict

import sqlalchemy
from app.models.categorie_model import Categorie
from flask import current_app, jsonify, request


def create():
    data = request.get_json()
    try:

        categorie = Categorie(**data)
        session = current_app.db.session

        session.add(categorie)
        session.commit()

        handle_categorie = asdict(categorie)
        handle_categorie['id'] = categorie.id
        handle_categorie['description'] = categorie.description

        return handle_categorie, 200

    except sqlalchemy.exc.IntegrityError:
        return {'msg': 'Category already exists!'}


def update(id: int):
    data = request.get_json()

    received_id = Categorie.query.filter_by(id=id).update(data)
    current_app.db.session.commit()
    categorie = Categorie.query.get(id)

    if received_id is 0:
        return {'msg': 'Category not found!'}, 404

    add_id_and_description = asdict(categorie)
    add_id_and_description['id'] = categorie.id
    add_id_and_description['description'] = categorie.description
    categorie = add_id_and_description

    return jsonify(categorie), 200


def delete(id: int):
    try:
        categorie = Categorie.query.get(id)

        current_app.db.session.delete(categorie)
        current_app.db.session.commit()

        return jsonify(categorie), 204

    except sqlalchemy.orm.exc.UnmappedInstanceError:
        return {'msg': 'category not Found!'}

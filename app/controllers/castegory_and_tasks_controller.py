from dataclasses import asdict

from app.models.categorie_model import Categorie
from flask import jsonify


def get_all():
    category = Categorie.query.all()
    output_list = []
    task_list = []
    for i, item in enumerate(category):
        categorie = asdict(category[i])
        categorie.pop('name')
        categorie['id'] = category[i].id
        categorie['name'] = category[i].name
        categorie['description'] = category[i].description

        for task in category[i].tasks:
            priority = task.eisenhower_classification.type
            assignment = asdict(task)
            assignment.pop('eisenhower_classification')
            assignment['priority'] = priority
            task_list.append(assignment)

        categorie['tasks'] = task_list
        output_list.append(categorie)

    return jsonify(output_list), 200

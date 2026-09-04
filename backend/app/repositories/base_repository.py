"""
Base Abstract Repository Pattern.
"""
from ..models import db

class BaseRepository:
    def __init__(self, model_class):
        self.model = model_class

    def get_by_id(self, entity_id):
        return self.model.query.get(entity_id)

    def get_all(self, page=None, per_page=None):
        query = self.model.query
        if page and per_page:
            pagination = query.paginate(page=page, per_page=per_page, error_out=False)
            return pagination.items, pagination.total
        return query.all(), len(query.all())

    def filter_by(self, page=1, per_page=20, **kwargs):
        query = self.model.query.filter_by(**kwargs)
        if page and per_page:
            pagination = query.paginate(page=page, per_page=per_page, error_out=False)
            return pagination.items, pagination.total
        items = query.all()
        return items, len(items)

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def update(self, entity_id, **kwargs):
        instance = self.get_by_id(entity_id)
        if not instance:
            return None
        for key, value in kwargs.items():
            if hasattr(instance, key) and value is not None:
                setattr(instance, key, value)
        db.session.commit()
        return instance

    def delete(self, entity_id):
        instance = self.get_by_id(entity_id)
        if not instance:
            return False
        db.session.delete(instance)
        db.session.commit()
        return True

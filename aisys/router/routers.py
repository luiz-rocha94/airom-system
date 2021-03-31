class DefaultRouter:
    """
    A router to control all database operations on models in the
    aisys applications.
    """
    route_app_labels = {'aisys'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read aisys models go to 'default'.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write aisys models go to 'default'.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the aisys app only appear in the 'default'.
        """
        if app_label in self.route_app_labels:
            return db == 'default'
        return None

class BaseRouter:
    """
    A router to control all database operations on models in the
    database applications.
    """
    route_app_labels = {'database'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read database models go to 'base'.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'base'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write database models go to 'base'.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'base'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the database app only appear in the 'base'.
        """
        if app_label in self.route_app_labels:
            return db == 'base'
        return None

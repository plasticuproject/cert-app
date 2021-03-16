class CertRouter(object):
    """
    A router to control all database operations on models in the
    certtool application.
    """
    route_app_labels = {'admin', 'auth', 'contenttypes', 'sessions'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read certs models go to certs database.
        """
        if model._meta.app_label == 'certtool':
            return 'cert_data'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write certs models go to the certs database.
        """
        if model._meta.app_label == 'certtool':
            return 'cert_data'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Do not allow relations involving the certs database
        """
        if obj1._meta.app_label == 'certtool' or \
           obj2._meta.app_label == 'certtool':
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Do not allow migrations on the certs database
        """
        if app_label in self.route_app_labels:
            return 'default'
        return False

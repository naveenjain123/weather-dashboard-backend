class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to dbread which selects replica from a weighted DNS
        """
        django_app = model._meta.app_label
        return "slave"

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_list = (
            "default",
            "slave",
        )
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All models end up in this pool.
        """
        return False

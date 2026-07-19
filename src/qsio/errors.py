class QSIOError(Exception):
    pass


class QSIOValidationError(QSIOError):
    pass


class CanonViolationError(QSIOValidationError):
    pass


class PermissionDeniedError(QSIOValidationError):
    pass


class QuietusError(QSIOError):
    pass

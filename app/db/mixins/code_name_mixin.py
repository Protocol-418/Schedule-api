from app.db.mixins.code_mixin import CodeMixin
from app.db.mixins.name_mixin import NameMixin

class CodeNameMixin(CodeMixin, NameMixin):
    pass

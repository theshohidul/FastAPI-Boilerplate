from sqlalchemy.orm import as_declarative


@as_declarative()
class Base:
    __name__: str

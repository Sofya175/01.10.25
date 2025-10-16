# Web-приложение
# Flask -SQLAlchemy - (ORM)

# from flask import Flask, url_for, request, render_template

import sqlalchemy as sa
from
from sqlalchemy.orm import Session

sqlalchemyBase = orm.declarative_base()

__factory = None


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Excep
from pytest import fixture
from sqlalchemy import create_engine

from db import Base
from settings.settings import POSTGRESQL, NAME
from settings.wsgi import create_wsgi

app = create_wsgi()


@fixture()
def client(init_database):  # pytest용 클라이언트
    return app.test_client()


@fixture(scope='session')
def database():  # pytest용 일회용 데이터베이스
    engine = create_engine('postgresql://postgres:root@127.0.0.1:5432', connect_args={'connect_timeout': 10})
    conn = engine.connect()
    conn.execute("COMMIT")

    conn.execute(f"DROP DATABASE IF EXISTS {NAME}")
    conn.execute("COMMIT")
    conn.execute(f"CREATE DATABASE {NAME}")
    conn.execute("COMMIT")
    conn.close()


@fixture()
def init_database(database):
    engine = create_engine(POSTGRESQL, connect_args={'connect_timeout': 10})
    Base.metadata.create_all(engine)

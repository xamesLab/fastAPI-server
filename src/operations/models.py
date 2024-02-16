from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

operation = Table(
    'operation',
    metadata,
    Column('id', Integer, primary_key=True),
    Column("quantity", String),
    Column("date", TIMESTAMP),
    Column("type", String),
    Column("instrument_type", String, nullable=True),
)

"""test_tric"""
from test_tric import DB


class State(DB.Model):
    """test_tric"""
    __tablename__ = 'states'

    id = DB.Column(DB.Integer, primary_key=True)
    service_name = DB.Column(DB.String(20), nullable=False)
    state_type = DB.Column(DB.Integer, nullable=False)
    state_datetime = DB.Column(DB.DateTime, nullable=False)
    info = DB.Column(DB.String())

    __table_args__ = (
        DB.Index('ix_service_type_dt', 'service_name', 'state_type', 'state_datetime'),
    )

    def __repr__(self) -> str:
        return f'<State: {self.service_name}-{self.id}>'

    def to_dict(self):
        """test_tric"""
        state_dict = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            state_dict[column.name] = str(value) if value else value
        return state_dict

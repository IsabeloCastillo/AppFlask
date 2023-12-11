import db
from sqlalchemy import Column, Integer, String, Boolean


class Tarea(db.Base):
    __tablename__='tarea'
    __table_args__ = {'extend_existing': True}  # Añade esta línea
    id = Column(Integer, primary_key=True)
    contenido = Column(String(100), nullable=False)
    hecha = Column(Boolean)


    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha


    def __repr__(self):
        return 'Tarea {}: {} ({})'.format(self.id, self.contenido, self.hecha)

    def __str__(self):
        return 'Tarea {}: {} ({})'.format(self.id, self.contenido, self.hecha)




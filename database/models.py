from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum as SQLEnum
)
from sqlalchemy.orm import relationship
from enum import Enum

from .database import Base


class Courses(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    directions = relationship("Directions", back_populates='course')


class Directions(Base):
    __tablename__ = "direction"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)

    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)

    course = relationship("Courses", back_populates="directions")
    lessons = relationship("Lesson", back_populates="direction")


class WeekType(Enum):
    add = "add"
    couple = "couple"
    all = "all"


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    aud = Column(String, nullable=False)
    teacher = Column(String, nullable=False)
    time = Column(String, nullable=False)
    day = Column(String, nullable=False)

    week_type = Column(SQLEnum(WeekType), default=WeekType.all, nullable=False)
    direction_id = Column(Integer, ForeignKey("direction.id"), nullable=False)
    
    direction = relationship("Directions", back_populates="lessons")

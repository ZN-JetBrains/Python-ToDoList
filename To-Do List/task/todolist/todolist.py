from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default="default_value")
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


engine = create_engine("sqlite:///todo.db?check_same_thread=False")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def print_menu():
    print("1) Today's tasks")
    print("2) Add task")
    print("0) Exit")


def run():
    while True:
        print_menu()
        user_input = int(input())

        if user_input == 0:
            print("\nBye!")
            break
        elif user_input == 1:  # Display all tasks
            print("\nToday:")
            # if not empty
            rows = session.query(Table).all()
            if len(rows) == 0:
                print("Nothing to do!\n")
            else:
                for index, row in enumerate(rows):
                    print(f"{index + 1}. {row.task}")
                print()

        elif user_input == 2:  # Add a row
            print("\nEnter task")
            user_task = input()
            new_row = Table(task=user_task,
                            deadline=datetime.strptime("01-24-2020", "%m-%d-%Y").date().today())
            session.add(new_row)
            session.commit()
            print("The task has been added!\n")


run()

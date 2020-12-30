from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from datetime import timedelta

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
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Add task")
    print("0) Exit")


def print_today_tasks():
    date = datetime.today()
    print(date.strftime("\nToday %#d %b:"))
    print_tasks(date)


def print_week_tasks(date):
    print(date.strftime("\n%A %#d %b:"))
    print_tasks(date)


def print_tasks(date):
    tasks = session.query(Table).filter(Table.deadline == date.date()).order_by(Table.deadline).all()

    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        for index, row in enumerate(tasks):
            print(f"{index + 1}. {row.task}")


def print_all_tasks():
    rows = session.query(Table).order_by(Table.deadline).all()
    
    if len(rows) == 0:
        print("Nothing to do!\n")
    else:
        print("\nAll tasks:")
        for index, row in enumerate(rows):
            date = datetime.strptime(str(row.deadline), "%Y-%m-%d").date()
            date = date.strftime("%#d %b")
            print(f"{index + 1}. {row.task}. {date}")


def run():
    while True:
        print_menu()
        user_input = int(input())

        if user_input == 0:
            print("\nBye!")
            break
        elif user_input == 1:  # Display all tasks for today
            print_today_tasks()
            print()
        elif user_input == 2:  # Display all tasks for this Week
            today = datetime.today()
            for day in range(7):
                current_date = today + timedelta(days=day)
                print_week_tasks(current_date)
            print()
        elif user_input == 3:  # Display all tasks in database
            print_all_tasks()
            print()
        elif user_input == 4:  # Add a row
            print("\nEnter task")
            user_task = input()
            print("Enter deadline")  # format: YYYY-MM-DD
            deadline_date = input()
            new_row = Table(task=user_task,
                            deadline=datetime.strptime(deadline_date, "%Y-%m-%d").date())
            session.add(new_row)
            session.commit()
            print("The task has been added!\n")


run()

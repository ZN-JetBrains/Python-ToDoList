from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from datetime import timedelta
from enum import IntEnum

Base = declarative_base()


class Menu(IntEnum):
    EXIT = 0,
    SHOW_TASKS_TODAY = 1,
    SHOW_TASKS_WEEK = 2,
    SHOW_TASKS_ALL = 3,
    SHOW_TASKS_MISSED = 4,
    ADD_TASK = 5,
    DELETE_TASK = 6


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
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")


def print_today_tasks():
    date = datetime.today()
    print(date.strftime("\nToday %#d %b:"))
    print_tasks(date)


def print_week_tasks():
    today = datetime.today()
    for day in range(7):
        current_date = today + timedelta(days=day)
        print(current_date.strftime("\n%A %#d %b:"))
        print_tasks(current_date)


def print_tasks(date):
    tasks = session.query(Table).filter(Table.deadline == date.date()).order_by(Table.deadline).all()

    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        for index, row in enumerate(tasks):
            print(f"{index + 1}. {row.task}")
    print()


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
    print()


def print_missed_tasks():
    print("\nMissed tasks:")
    rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    if len(rows) == 0:
        print("Nothing is missed!")
    else:
        for index, row in enumerate(rows):
            date = datetime.strptime(str(row.deadline), "%Y-%m-%d").date()
            date = date.strftime("%#d %b")
            print(f"{index + 1}. {row.task}. {date}")
    print()


def add_task():
    print("\nEnter task")
    user_task = input()
    print("Enter deadline")  # format: YYYY-MM-DD
    deadline_date = input()
    new_row = Table(task=user_task,
                    deadline=datetime.strptime(deadline_date, "%Y-%m-%d").date())
    session.add(new_row)
    session.commit()
    print("The task has been added!\n")


def delete_task():
    rows = session.query(Table).order_by(Table.deadline).all()

    if len(rows) == 0:
        print("Nothing to delete!\n")
    else:
        print("\nChoose the number of the task you want to delete:")
        for index, row in enumerate(rows):
            date = datetime.strptime(str(row.deadline), "%Y-%m-%d").date()
            date = date.strftime("%#d %b")
            print(f"{index + 1}. {row.task}. {date}")
    task_to_delete = int(input())
    specific_row = rows[task_to_delete - 1]
    session.delete(specific_row)
    session.commit()
    print("The task has been deleted!\n")


def process_input():
    user_input = int(input())

    if user_input == Menu.EXIT:
        print("\nBye!")
        return False
    elif user_input == Menu.SHOW_TASKS_TODAY:  # Display all tasks for today
        print_today_tasks()
    elif user_input == Menu.SHOW_TASKS_WEEK:  # Display all tasks for this Week
        print_week_tasks()
    elif user_input == Menu.SHOW_TASKS_ALL:  # Display all tasks in database
        print_all_tasks()
    elif user_input == Menu.SHOW_TASKS_MISSED:  # Display missed tasks
        print_missed_tasks()
    elif user_input == Menu.ADD_TASK:  # Add a row
        add_task()
    elif user_input == Menu.DELETE_TASK:  # Delete task
        delete_task()
    return True


def run():
    is_running = True
    while is_running:
        print_menu()
        is_running = process_input()


run()

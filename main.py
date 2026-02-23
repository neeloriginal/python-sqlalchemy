#import
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

#connect to database
engine = create_engine('sqlite:///tasks.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#define model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    task = relationship("Task", back_populates= "user", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="task")

Base.metadata.create_all(engine)

#utility Function
def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def confirm_action(prompt:str) -> bool:
    return input(f"\n{prompt} (yes/no): ").lower().strip() == 'yes'

#crud ops
def add_user():
    name, email = input("Enter Username: "), input("Enter Email: ")
    if get_user_by_email(email):
        print(f"User already exists: {email}")
        return
    try:
        session.add(User(name=name, email=email))
        session.commit()
        print(f"User added: {name}")
    except IntegrityError:
        session.rollback()
        print("Error adding user.")

def add_task():
    email = input("Enter the email of the user to add tasks: ")
    user = get_user_by_email(email)
    if not user:
        print(f"No user found with this {email}.")
        return
    title, description = input("Enter Task Title: "), input("Enter Task Description: ")
    session.add(Task(title=title, description=description, user_id=user.id))
    session.commit()
    print(f"Task added to database {title}: {description}")

#query
def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.name},Email: {user.email}")

def query_tasks():
    email = input("Enter the email of the user for tasks: ")
    user = get_user_by_email(email)
    if not user:
        print("There is no user with this {email} email")
        return
    
    for task in user.task:
        print(f"Task ID: {task.id}, Title: {task.title}, Description: {task.description}")
        
def update_user():
    email = input("Enter the email of the user to update: ")
    user = get_user_by_email(email)
    if not user:
        print("No user found with this email.")
        return
    new_name = input("Enter the new name (leave blank to keep current): ")
    if new_name:
        user.name = new_name
    new_email = input("Enter the new email (leave blank to keep current): ")
    if new_email:
        user.email = new_email
    session.commit()
    print("User updated successfully.")

#deleteing user and task
def delete_user():
    email = input("Enter the email of the user to delete: ")
    user = get_user_by_email(email)
    if not user:
        print("No user found with this email.")
        return
    if confirm_action(f"Are you sure you want to delete user {user.name} and all their tasks?"):
        session.delete(user)
        session.commit()
        print("User and their tasks deleted successfully.")
    else:
        print("Deletion cancelled.")

def delete_task():
    email = input("Enter the email of the user for task deletion: ")
    user = get_user_by_email(email)
    if not user:
        print("No user found with this email.")
        return
    if not user.task:
        print("This user has no tasks to delete.")
        return
    for task in user.task:
        print(f"Task ID: {task.id}, Title: {task.title}")
    try:
        task_id = int(input("Enter the Task ID to delete: "))
    except ValueError:
        print("Invalid Task ID.")
        return
    task_to_delete = session.query(Task).filter_by(id=task_id, user_id=user.id).first()
    if not task_to_delete:
        print("No task found with this ID for the specified user.")
        return
    if confirm_action(f"Are you sure you want to delete task '{task_to_delete.title}'?"):
        session.delete(task_to_delete)
        session.commit()
        print("Task deleted successfully.")
    else:
        print("Deletion cancelled.")

#main function
def main()->None:
    actions = {
        "1" : add_user,
        "2" : add_task,
        "3" : query_users,
        "4" : query_tasks,
        "5" : update_user,
        "6" : delete_user,
        "7" : delete_task,
        "8" : exit
    }
    while True:
        print("\nOptions:\n1. Add User\n2. Add Task\n3. Query Users\n4. Query Tasks\n5. Update User\n6. Delete User\n7. Delete Task\n8. Exit")
        choice = input("Enter your choice: ")
        if choice == "8":
            print("Adios....")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("That is not an option")

if __name__ == "__main__":
    main()
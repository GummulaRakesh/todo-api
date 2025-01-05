from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import create_access_token, get_current_user
from database import SessionLocal, Task
from schemas import TaskCreate, TaskUpdate, TaskResponse, Login  # Import the Login model

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dummy user database
USERS_DB = {"admin": "password123"}

# 1. User Login Endpoint - uses Login Pydantic model
@app.post("/login")
def login(login_data: Login):
    if login_data.username in USERS_DB and USERS_DB[login_data.username] == login_data.password:
        token = create_access_token(data={"sub": login_data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# 2. Protected Endpoints - Create Task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    try:       
        if task.description is None:
            raise HTTPException(status=404, detail="discription is empty")
        new_task = Task(title=task.title, description=task.description)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except:
        raise HTTPException(status_code=404,detail="Failed to add task")
    
# 3. Protected Endpoints - Get All Tasks
@app.get("/tasks", response_model=list[TaskResponse])
def fetch_tasks(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(Task).all()

# 4. Protected Endpoints - Get Single Tasks
@app.get("/tasks/{id}", response_model=TaskResponse)
def fetch_task(id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# 5. Protected Endpoints - Update Single Task
@app.put("/tasks/{id}", response_model=TaskResponse)
def update_task(id: int, update_data: TaskUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = update_data.status
    task.title = update_data.title
    task.description = update_data.description
    db.commit()
    db.refresh(task)
    return task

# 6. Protected Endpoints - Delete Single Task
@app.delete("/tasks/{id}", response_model=dict)
def delete_task(id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import (create_new_job,
        retreive_job,list_jobs,
        update_job_by_id,
        delete_job_by_id)
from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from typing import List

router = APIRouter()


@router.post("/create-job",response_model=ShowJob)
def create_job(job : JobCreate,db : Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job

from fastapi import APIRouter, Depends, HTTPException

from db.database import get_db
from models.job import StoryJob
from schemas.job import StoryJobResponse

router = APIRouter(
    prefix='/jobs',
    tags=['jobs'],
)


@router.get('/{job_id}', response_model=StoryJobResponse)
def get_job(job_id: str, db=Depends(get_db)) -> StoryJobResponse:
    job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail='Job not found')

    return StoryJobResponse(
        job_id=job.job_id,
        status=job.status,
        created_at=job.created_at,
        story_id=job.story_id,
        completed_at=job.completed_at,
        error=job.error
    )

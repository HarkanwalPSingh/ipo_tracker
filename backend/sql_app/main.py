from datetime import date
from importlib import reload
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import uvicorn
from fastapi.templating import Jinja2Templates

import crud, models, schemas
from database import SessionLocal, engine
from config import settings

CURR_DATE = date.today()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory="templates")

@app.get('/form')
def form_post(request: Request):
    id = 'Type IPO ID'
    return templates.TemplateResponse('ipo.html', context={'request': request, 'id': id})


@app.post('/form')
def form_post(request: Request, id: int = Form(...), db: Session = Depends(get_db)):
    ipo = crud.get_ipo(db, id=id)
    return templates.TemplateResponse('ipo.html', context={'request': request, 'company': ipo.company, \
                                      'open_date' : ipo.open_date, 'close_date' : ipo.close_date, \
                                      'lot_size' : ipo.lot_size, 'issue_price' : ipo.issue_price, \
                                      'cost_of_one_lot' : ipo.cost_of_one_lot})


@app.get("/ipos/{id}", response_model=schemas.IPO)
async def read_ipo(id: int, db: Session = Depends(get_db)):
    ipo = crud.get_ipo(db, id=id)
    if not ipo:
        raise HTTPException(status_code=404, detail="IPO not found")
    return ipo

@app.get("/ipos/", response_model=Optional[list[schemas.IPO]])
async def read_month_ipo(year:int, month:str, db: Session = Depends(get_db)):
    ipo = crud.get_month_ipo(db,year,month)
    if not ipo:
        raise HTTPException(status_code=404, detail="No IPO found")
    return ipo

@app.get("/ipos/date/{curr_date}", response_model=list[schemas.IPO])
def read_ipo_date(curr_date: date, db: Session = Depends(get_db)):
    ipo = crud.get_ipo_date(db, curr_date=curr_date)
    if not ipo:
        raise HTTPException(status_code=404, detail="IPO not found")
    return ipo

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )


# uvicorn sql_app.main:app --reload

# @app.get("/ipos/date/{curr_date}", response_model=list[schemas.IPO])
# def read_ipo_date(curr_date: date, db: Session = Depends(get_db)):
#     ipo = crud.get_ipo_date(db, curr_date=curr_date)
#     if not ipo:
#         raise HTTPException(status_code=404, detail="IPO not found")
#     return ipo

# @app.get("/ipos/year/{year}/month/{month}", response_model=Optional[list[schemas.IPO]])
# async def read_month_ipo(year:int, month:str, db: Session = Depends(get_db)):
#     ipo = crud.get_month_ipo(db,year,month)
#     if not ipo:
#         raise HTTPException(status_code=404, detail="No IPO found")
#     return ipo

# @app.get("/ipos/company/{company}", response_model=schemas.IPO)
# def read_ipo_company(company: str, db: Session = Depends(get_db)):
#     ipo = crud.get_ipo_company(db, company=company)
#     if not ipo:
#         raise HTTPException(status_code=404, detail="IPO not found")
#     return ipo

# @app.get("/ipos/active/", response_model=Optional[list[schemas.IPO]])
# def read_active_ipo(db: Session = Depends(get_db)):
#     ipo = crud.get_active_ipo(db,curr_date=CURR_DATE)
#     return ipo

# uvicorn sql_app.main:app --reload
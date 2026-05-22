from fastapi import FastAPI
from src.api.routers.books import router as books_router
from src.api.routers.members import router as members_router
from src.api.routers.borrow import router as borrow_router
from src.api.routers.auth import router as auth_router
# from src.api.router.products import router as product_router 

app = FastAPI()

app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(members_router, prefix="/members", tags=["Members"])
app.include_router(borrow_router, prefix="/borrow", tags=["Borrow"])
app.include_router(auth_router,prefix="/auth",tags=["Auth"])
# app.include_router(product_router,prefix="/product",tags=["Product"])

@app.get("/")
def read_root():
    return {"message": "API Running"}

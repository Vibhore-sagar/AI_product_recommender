from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import RecommendationRequest
from app.recommender import get_ai_recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/recommend")
def recommend_products(request: RecommendationRequest):
    ai_output = get_ai_recommendations(
        request.preference,
        request.products
    )

    recommended_names = [name.strip() for name in ai_output.split(",")]

    filtered_products = [
        p for p in request.products if p.name in recommended_names
    ]

    return filtered_products

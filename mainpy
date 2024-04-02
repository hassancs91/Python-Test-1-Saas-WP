from fastapi import FastAPI

app = FastAPI()

@app.get("/titles")
def get_titles():
    # Example list of titles
    titles = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "Moby-Dick"]

    # Returning the data in the specified format
    return {
        "success": True,
        "message": "Endpoint Test Completed Successfully",
        "result": titles
    }

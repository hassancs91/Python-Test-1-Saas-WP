from fastapi import FastAPI

app = FastAPI()

@app.get("/titles")
def get_titles(keyword: str = None):
    # Example list of titles
    titles = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "Moby-Dick"]

    # Filter titles if keyword is provided
    if keyword:
        filtered_titles = [title for title in titles if keyword.lower() in title.lower()]
    else:
        filtered_titles = titles

    # Returning the data in the specified format
    return {
        "success": True,
        "message": "Endpoint Test Completed Successfully",
        "result": filtered_titles
    }

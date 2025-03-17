from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///somakodi.db", echo = True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM students"))
    for row in result:
        print(row)
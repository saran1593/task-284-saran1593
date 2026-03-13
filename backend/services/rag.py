from groq import Groq
from sqlalchemy.orm import Session
from sqlalchemy import text
import re

client = Groq(api_key="")

def question_to_sql(question: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "user",
            "content": f"""You are the sqlite expert. Convert the following question to SQLite query: {question}
            table name: users
            columns: id(integer), name(string), email(string), password(string)
            
            Guardrails:
            - Only generate SQLite queries.
            - Do not include any explanations, only provide the SQLite query.
            - Use only the provided table and columns.
            - Donot hallucinate table or column names.""" 
        }
        ],
    )
    return completion.choices[0].message.content.strip()

def run_query(db:Session, query: str):
    result = db.execute(text(query))
    rows = result.fetchall()
    return rows

def format(query: str) -> str:
    query = re.sub(r"```sql","",query,flags=re.IGNORECASE)
    query = re.sub(r"```","",query)
    return query.strip()

def output_response(result: str, question: str, query: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "user",
            "content": f""" explain the results {result} of the following query in context of the question: {question} and query: {query}
            give the response for result only. Donot include questions and sql query in the response. 
            example: if question is "how many users are there?" and result is "[(5,)]" then response should be "There are 5 users.  """
        }
        ],
    )
    return completion.choices[0].message.content.strip()

def rag_pipeline(db:Session, question: str):
    sql = question_to_sql(question)
    formatedsql = format(sql)
    result = run_query(db, formatedsql)
    return output_response(result, question, formatedsql)
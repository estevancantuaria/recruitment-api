from datetime import datetime

def convert_string_to_date(data_nascimento: str) -> datetime:
    return datetime.strptime(data_nascimento, "%Y-%m-%d").date()
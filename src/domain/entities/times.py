from pydantic import BaseModel






class Times(BaseModel):
    turn: str
    classroom: str
    time: dict = {
        "segunda-feira": {
            "13:05-13:45": "Nicomedos Kialanda",
            "13:45-14:45": "Nicomedos Kialanda",
            "14:45-15:25": "Joaquim Mbala",
            "15:45-16:30": "António Campos",
            "16:30-17:20": "António Campos",
            "17:20-18:05": "António Campos"
        },
        "terca-feira": {
            "13:05-13:45": "Marcial de Seabra",
            "13:45-14:45": "Marcial de Seabra",
            "14:45-15:25": "Marcial de Seabra",
            "15:45-16:30": "António Campos",
            "16:30-17:20": "António Campos",
            "17:20-18:05": "António Campos"
        },
        "quarta-feira": {
            "13:05-13:45": "Marcial de Seabra",
            "13:45-14:45": "Marcial de Seabra",
            "14:45-15:25": "Marcial de Seabra",
            "15:45-16:30": "Marcial de Seabra",
            "16:30-17:20": "Nicodemos Kialanda",
            "17:20-18:05": "Nicodemos Kialanda"
        },
        "quinta-feira": {
            "13:05-13:45": "Joaquim Mabala",
            "13:45-14:45": "Joaquim Mabala",
            "14:45-15:25": "Marcial de Seabra",
            "15:45-16:30": "Marcial de Seabra",
            "16:30-17:20": "borla",
            "17:20-18:05": "borla"
        },
        "sexta-feira": {
            "13:05-13:45": "Heldér Joaquim",
            "13:45-14:45": "Heldér Joaquim",
            "14:45-15:25": "Joaquim Mabala",
            "15:45-16:30": "Joaquim Mabala",
            "16:30-17:20": "Marcial de Seabra",
            "17:20-18:05": "Marcial de Seabra"
        }
    }

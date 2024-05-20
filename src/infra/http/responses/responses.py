


class Response:
    def get_students(datas: list) -> list:
        """create response for datas students"""
        dics = []
        for data in datas:
            dics.append({
                "id": data[0],
                "name": data[1],
                "grade": data[2],
                "course": data[3],
                "classroom": data[4],
                "turn": data[5],
                "photo": data[6],
            })
        return dics

    def get_teachers(datas: list) -> list:
        """create response for datas teachers"""
        dics = []
        for data in datas:
            dics.append({
                "id": data[0],
                "name": data[1],
                "turn": data[2],
                "photo": data[3],
                "subject": data[4],
            })
        return dics
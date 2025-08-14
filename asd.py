#Приложения для отбора музыки, пользователь вводит критерий

data_of_music = {
    'songs' : [
        {"tittle": "asd", "artist": "me", "genre": "stress"},
        {"tittle": "haha", "artist": "not me", "genre": "hipe"}        
    ]
    }

def GetValue(data: list, type: str, choice: str):
    if data:
        for dat in data['songs']:
            if type is "tittle":
                
    else:
        return "Ошибка данные пустые"    
    
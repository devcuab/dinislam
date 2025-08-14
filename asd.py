#Приложения для отбора музыки, пользователь вводит критерий

data_of_music = {
    'songs' : [
        {"tittle": "asd", "artist": "me"},
        {"tittle": "haha", "artist": "not me"}        
    ]
    }

def GetValue(data: list, type: str, choice: str):
    if data:
        if type == "tittle":
            result = next(filter(lambda da: da["tittle"] == choice, data['songs']))
            if result:
                return_data = ""
                for res in result:
                    return_data += f"песня: (титул:{res["tittle"]}, исполнитель:{res["artist"]}) \n"
                return return_data
            else:
                return "Песни не были найдены"
        
                
        if type == "artist":
            result = next(filter(lambda da: da["artist"] == choice, data["songs"]))
            if result:
                return_data = ""
                for res in result:
                    return_data += f"песня: (титул:{res["tittle"]}, исполнитель:{res["artist"]}) \n"
                return return_data
            else:
                return "Песни не были найдены"
    else:
        return "Ошибка данные пустые"    
    

if __name__ == "__main__":
    while True:
        choised_type = input("Введите по какому критерию будет поиск: (исполнитель \ титул)")
        if choised_type != "исполнитель" or choised_type != "титул":
            print("Ошибка: не корректный выбор")
        choised_ch = input("Введите поиск по выбранному критерию")
        print(GetValue(data=data_of_music, type=choised_type, choice=choised_ch))
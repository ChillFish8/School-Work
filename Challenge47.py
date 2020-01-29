Results_Dict = {}


def InputData():
    global Results_Dict
    User_Input = input("What is your name? ")
    User_Score = input("What was your score? ")
    User_Subject = input("What Subject was this? ")
    if User_Subject in Results_Dict:
        TempList = Results_Dict[User_Subject]
        TempList.append({
            'name': User_Input,
            'score': User_Score
            })
        Results_Dict[User_Subject] = TempList

    else:
        TempList = [{
            'name': User_Input,
            'score': User_Score
        }]
        Results_Dict[User_Subject] = TempList


def ListAllScores():
    global Results_Dict
    for key in Results_Dict:
        print(f"======== {key} ==========")
        for item in Results_Dict[key]:
            print(f"User: {item['name']}, Subject: {key}, Score: {item['score']}")


def ListSubjectScores(Subject):
    global Results_Dict
    for item in Results_Dict[Subject]:
        print(f"User: {item['name']}, Score: {item['score']}")


def GetUserScores(UserName):
    global Results_Dict
    for key in Results_Dict:
        for user in Results_Dict[key]:
            if UserName in user:
                print(f"User: {user['name']}, Subject: {key}, Score: {user['score']}")


if __name__ == "__main__":
    InputData()
    InputData()
    InputData()
    ListAllScores()
    GetUserScores("Harry")
    ListSubjectScores("Maths")

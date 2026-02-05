print("welcome to treasure Hunt Game \n choose the options and you might win the treasure")

answer = "continue"
while answer == "continue":
    value1 = input("you are a crossroad, where do you wanna go, left ? or right ?")
    if value1 == "left":
        print("you chose wrong , left lead to lava")
        answer= input("continue to replay , anything else  to exit")

    elif value1 == "right":
        print("yeah ! go ahead ")
        value2 = input("you reached a river , options boat or fancy river raft")
        if value2 == "boat":
            print("sorry, boat had a hole ")
            answer = input("continue to replay , anything else  to exit")
        elif value2 == "river raft":
            print("ahaa ! treasure")
            answer= 0
        else:
            print("can't trick me just choose from the above options")
            answer = input("continue to replay , anything else  to exit")
    else :
        print("can't trick me just choose from the above options")
        answer = input("continue to replay , anything else  to exit")


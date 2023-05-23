# coding=utf-8

def GenUsers():
    from User import User
    from GlobalVariable import global_obj
    import random
    for i in range(10000):
        user = User(random.randint(0, 4), random.randint(0, 1), random.randint(0, 5), i)
        global_obj.add_user_to_list(user)
from .models import User
from api.utils import checkUser
def changePass(username,passOld,passNew):
    if checkUser(username,passOld):
        user = User.objects.get(username=username)
        # print(user)
        # print(user.diachi)
        user.set_password(passNew)
        user.save()
        return True
    return False
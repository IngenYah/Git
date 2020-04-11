#定义开始界面
def main_interface():
    a = input('Welcome to the system\nPlease choose the sector you want to enter\n1.Building new member\n2.View member database\nPress the corresponding sign:')
    return a

#新建用户
def new_member():
    new_members.append(input("Input member's first name:"))
    new_members.append(input("Input member's last name:"))
    new_members.append(input("Input member's sex:"))
    new_members.append(input("Input member's age:"))
    new_members.append(input("Input member's country:"))
    return new_members

#用户信息
class new_member_information():
    def __init__(self,sign,first_name,last_name,sex,age,country):
            self.sign = sign
            self.name = last_name +' '+ first_name
            self.sex = sex
            self.age = age
            self.country = country
    def member_information(self):
            print(self.sign,'.Name:',self.name,' Sex:',self.sex,' Age:',self.age,' Country:',self.country,'\n')

new_members = []
members = []
i = 1
while True:
    user_selected = main_interface()
    if user_selected == '1':
        print('BUILDING NEW MEMBER')
        new_member()
        members.append(new_member_information(i,new_members[0],new_members[1],new_members[2],new_members[3],new_members[4]))
        new_members = []
        i = i + 1

    elif  user_selected == '2':
        print('MEMBER DATABASE')
        for member in members:
            member.member_information()
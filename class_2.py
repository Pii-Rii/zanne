
#메소드오버라이딩


class unit:
    def __init__(self, name, hp):  #생성자의 2개 전달값(파라미터; 함수에 이용할 변수)
        self.name=name            #클래스 내부에서 멤버변수 생성  self.멤버변수명=값
        self.hp=hp
        print("{0} 유닛이 생성되었습니다 [체력:{1}]".format(self.name, self.hp)) #클래스 내부에서 멤버변수 접근   self.멤버변수명
        
    def move(self, location):
        print("[지상이동] {0}: {1}방향으로 이동합니다".format(self.name, location))   
    

class attack_unit(unit):  #부모클래스 상속
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)  #부모클래스의 생성자 호출
        self.damage=damage

    def attack(self, location):
        print("{0}가 {1}방향으로 공격합니다".format(self.name, location))    

    def damaged(self, damage):
        print("{0}: 데미지를 입었습니다".format(self.name))
        self.hp-=damage
        print("{0}의 현재 체력:{1}".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}: 파괴되었습니다".format(self.name))

# 
class flyable:
    def __init__(self, flying_spd):
        self.flying_spd=flying_spd

    def fly(self, name, location):
        print("{0}: {1}방향으로 날아갑니다 [속도:{2}]".format(name,location,self.flying_spd))

#다중상속
class flyable_attackunit(attack_unit,flyable):
    def __init__(self,name,hp,damage,flying_spd):
        attack_unit.__init__(self,name,hp,damage)
        flyable.__init__(self,flying_spd)
    def move(self, location):
        print("[공중이동] {0}: {1}방향으로 이동합니다".format(self.name, location))



medic1=unit("메딕", 20)
medic2=unit("메딕",20)
medic1.attack= True  #클래스 객체에 특정 멤버변수 부여; 클래스외부에서 멤버변수 생성   객체.멤버변수명
if medic1.attack == True:
    print("{0}: 공격력을 얻었습니다".format(medic1.name))  #클래스외부에서 멤버변수 접근   객체.멤버변수명


marine1=attack_unit("마린",30,5)
marine1.attack(2)
marine1.damaged(10)


valkyrie1=flyable_attackunit("발키리",40,15,10)
valkyrie1.fly(valkyrie1.name,2)

medic1.move("11시")
valkyrie1.move("10시")







class Unit(object):
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life
        
    def show_status(self):
        print('이름: {}'.format(self.name))
        print('등급: {}'.format(self.rank))
        print('사이즈: {}'.format(self.size))
        print('라이프: {}'.format(self.life))
        

class Goblin(Unit):
    # damage 속성 추가
    def __init__(self, rank, size, life, attack_type, damage):
        super(Goblin, self).__init__(rank, size, life)
        self.attack_type = attack_type
        self.damage = damage
        
    def show_status(self):
        super(Goblin, self).show_status()
        print('공격 타입: {}'.format(self.attack_type))
        # 오버라이드 메소드
        print ('데미지: {}'.format(self.damage))
        
        
    # 공격 메소드 추가
    def attack(self):
        print('[{}]이 공격합니다! 상대방 데미지({})'.format(self.name, self.damage))
        

class SphereGoblin(Goblin):
    def __init__(self, rank, size, life, attack_type, damage, sphere_type):
        super().__init__(rank, size, life, attack_type, damage)
        self.sphere_type = sphere_type
        
    def show_status(self):
        super().show_status()
        print('창 타입: {}'.format(self.sphere_type))
        

sphere_goblin_1 = SphereGoblin('병사', 'Small', 100, '레인지 공격', 10, '긴 창')

sphere_goblin_1.show_status()
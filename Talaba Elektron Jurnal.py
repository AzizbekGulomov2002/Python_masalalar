class Talaba():
    def __init__(self,ism,familiya,tel,manzili):
        self.ism =ism
        self.familiya = familiya
        self.tel = tel
        self.manzili = manzili
    @property
    def ism(self):
        return self.__ism
    @ism.setter
    def ism(self,ism):
        if len(ism)>2:
            self.__ism = ism
        else:
            raise Exception('ism uchta belgidan kam bo\'lishi mumkin emas. ')
    @property
    def familiya(self):
        return self.__familiya
    @familiya.setter
    def familiya(self,familiya):
        if len(familiya)>2:
            self.__familiya = familiya
        else:
            raise Exception('familiya uchta belgidan kam bo\'lishi mumkin emas. ')
    @property
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self,tel):
        if len(tel)==7 or len(tel)==9 or len(tel)==13:
            self.__tel = tel
        else:
            raise Exception('tel 7,9,13 ta belgi bo\'lishi kerak. ')
    @property
    def manzili(self):
        return self._manzili
    @manzili.setter
    def manzili(self,manzili):
        if len(manzili)>2:
            self._manzili = manzili
        else:
            raise Exception("Manzili 3ta belgidan kam bo`lmasin!!")
class Talaba_Guruhi:
    talabalar=[
        Talaba('asd','asdf','998887799',"Qarshi shahar"),
        Talaba('basd','asdf','+998978566585', "Qarshi shahar"),
        

        ]
    

    def talaba_qushish(self):
        print('Yangi talaba qushish:')
        ism = input('ismni kiriting:> ')
        familiya = input('familiya kiriting:> ')
        tel = input('tel ni kiriting:> ')
        manzili = input("Manzilini kiriting: >")
        self.talabalar.append(Talaba(ism,familiya,tel,manzili))  
    
    def chiqarish(self):
        print('O`rni|','ism|','familiya|','telefon nomer|',"Yashash Manzili")
        for index,i in enumerate(self.talabalar,start=0):
            print(index,'|', i.ism,'|',i.familiya,'|',i.tel, "|",i.manzili)

    def uchirish(self):
        while True:
                
            self.chiqarish()
            try:
                m =int(input("O'chirmoqchi bo'lgan talabangizni T/r sini kiriting: "))
                if m>=0 and m<len(self.talabalar):
                    self.talabalar.remove(self.talabalar[int(m)])
                    self.chiqarish()
                else:
                    print('Qaytadan kiritib ko\'ring T/r kiritishda xatolik')
                    
                
            except:
                print('Siz raqam kiritmadiz. E\'tiborli bo\'ling')
            m = input('Amalni to`xtatmoqchimisiz: (1/0): ')

            if m=='1':
                break
        

    def saralash(self):
        m = input("Qaysi nom bo'yicha saralamoqchisiz? ")
        if m=='ism':
            self.talabalar.sort(key=lambda x: x.ism)
        elif m=='familiya':
            self.talabalar.sort(key=lambda x: x.familiya)
        elif m=='tel':
            self.talabalar.sort(key=lambda x: x.tel)
        else:
            print('xato qaytadan urinib ko\'ring. ')


    
tg = Talaba_Guruhi()
while True:

    m = input('Amalni tanlang:(1-chiqarish, 2-qushish,3-o\'chirish,4-saralash, 0-dasturdan chiqish):> ')

    if m=='1':
        tg.chiqarish()
    elif m=='2':
        tg.talaba_qushish()
    elif m=='0':
        break
    elif m=='4':
        tg.saralash()
    elif m=='3':
        tg.uchirish()



    


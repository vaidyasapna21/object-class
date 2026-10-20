class stationery:
  def __init__(self,name,price,qty):
    self.name=name
    self.price=price
    self.qty=qty
        
    
s1 = stationery( "pencil",10,50)
s2 = stationery( "notbook",50,75)
s3 = stationery( "comic-book",45,24)
s4 = stationery( "novel",70,110)
s5 = stationery( "blue-pen",20,60)
s6 = stationery( "eraser",5,57)
s7 = stationery( "highliter",30,66)

stationery_list=[]
stationery_list.append(s1)
stationery_list.append(s2)
stationery_list.append(s3)
stationery_list.append(s4)
stationery_list.append(s5)
stationery_list.append(s6)
stationery_list.append(s7)

for i in stationery_list:
    if i.qty> 70:
        print(i.qty)
    #print(i.name.i.price,i.qty)

          
class cloths:
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty
        
p1=cloths("punjabi",750,55) 
p2=cloths("banarasi-saree",2000,45)
p3=cloths("Anrkali",1200,37) 
p4=cloths("kurti",900,78) 
p5=cloths("lehanga",2900,25) 
p6=cloths("cordsrt",2500,56) 
p7=cloths("one-piece",2700,33) 

cloths_list=[]
cloths_list.append(p1)
cloths_list.append(p2)
cloths_list.append(p3)
cloths_list.append(p4)
cloths_list.append(p5)
cloths_list.append(p6)
cloths_list.append(p7)

for items in cloths_list:
    #print(items.name,items.price,items.qty)
    if items.price>=2000:
        print(items.price)
        
        
        
class car:
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty        

a1=car("tata punch",600000,9)
a2=car("maroti suzuki swift",700000,7)
a3=car("tata nexon",800000,5)
a4= car("mahindra thar",1000000,8)
a5=car("hyndai crata",1100000,6)

car_list=[]
car_list.append(a1)
car_list.append(a2)
car_list.append(a3)
car_list.append(a4)
car_list.append(a5)

for c in car_list:
    if c.price>= 600000:
        print(c.price)





  
       
    

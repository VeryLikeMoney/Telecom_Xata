import math

class Main_Parametrs:
    NAME_PARAMETR=("f",'d','h_b','h_m')

    def __init__(self,inp_patamet:dict) -> None:
        try:
            for key,val in inp_patamet.items():
                if key in self.NAME_PARAMETR:
                    self.__setattr__(key,float(val))
        except:
            pass

class L (Main_Parametrs):
    def calculation_L(self):
        l=0
        if self.f<=30:
            l=self.L_to_30MG()
        elif 30<=self.f<=150:
            l=self.L_from_30_to_150MG()
        elif 150<self.f<=1500:
            l=self.L_from_150_to_1500MG()
        elif 1500<=self.f<2000:
            l=self.L_from_1500_to_2000MG()
        elif 2000<=self.f<=3000:
            l=self.L_from_2000_to_3000MG()
        return l
    

    def L_to_30MG(self)->float:
        l=32.5+20*math.log10(self.f)+20*math.log10(self.d)
        return l
    def L_from_30_to_150MG(self)->float:
        a1=69.55+26.16*math.log10(150)-20*(150/self.f)
        b1=-13.82*math.log10(self.h_b)
        c1=(44.9-6.55*math.log10(self.h_m))*math.log10(self.d)
        a_h=(1.1*math.log10(self.f)-0.7)*self.h_m-(1.56*math.log10(self.f)-0.8)
        return a1+b1+c1+a_h
    def L_from_150_to_1500MG(self)->float:
        a1=68.75+(44.9-6.55*math.log10(self.h_b))*math.log10(self.d)
        b1=(27.72-1.1*self.h_m)*math.log10(self.f)
        c1=-13.82*math.log10(self.h_b)+0.7*self.h_m
        return a1+b1+c1
    def L_from_1500_to_2000MG(self)->float:
        a1=45.5+(44.9-6.55*math.log10(self.h_b))*math.log10(self.d)
        b1=(35.46-1.1*self.h_m)*math.log10(self.f)
        c1=-13.82*math.log10(self.h_b)+0.7*self.h_m
        return a1+b1+c1
    def L_from_2000_to_3000MG(self)->float:
        a1=124.4+(44.9-6.55*math.log10(self.h_b))*math.log10(self.d)
        b1=(11.56-1.1*self.h_m)*math.log10(self.f)
        c1=-13.82*math.log10(self.h_b)+0.7*self.h_m
        return a1+b1+c1

def out_L(parametr:dict)->str:
    l_out=L(parametr).calculation_L()
    return str(round(l_out,3))

if __name__=='__main__':
    d={'f': '1600', 'd': '2', 'h_b': '30', 'h_m': '2'}
    print(out_L(d))
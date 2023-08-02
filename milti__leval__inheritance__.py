class Dad:
    basketball=6

class Son(Dad):
    dance=1
    basketball = 9
    def isdance(self):
        return f"Yes i dance {self.dance} no of time"

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"yes i dance very awsomely{self.dance} noo off time "

darry = Dad()
larry = Son()
harry = Grandson()
print(harry.isdance())

# class Pr():
#     basketball=1
# -----------------------This is multilevel inheritance--------------------------
# class jj(Pr):
#     basketball = 4
#
#     def pra(self):
#         return f"yes i prastic every day{self.pra}"
#
# class Stavan(jj):
#     def pra(self):
#         return f"ok bhai jii i prastic every day{self.pra}"
#
# Dada=Pr()
# papa=jj()
# its_me=Stavan()
#
# print(Dada.basketball)
# print(its_me.basketball)



























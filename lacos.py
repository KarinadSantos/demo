
mat: str = input("matricula:")
while(len(mat) != 14) or (not mat.isdigit()):
   mat = input("matricula:")


ano: str = mat [0:4]
período:str = mat [4]
curso: str = mat [5:8]
id_mat: str = mat [-3:]

print(ano)
print(período)
print(curso)
print(id_mat)

glb_var= "global"

def var_function():
    lcl_var = "local"
    print(lcl_var)
    print(glb_var) #Print glb_var within function

var_function()
print(glb_var)

import methods.function as function
def defFunction(strFunc,type):
    newStr = strFunc.replace("e","E").replace("pi","PI")
    func = ""
    if(type == "f"):
        func = function.fDef(newStr)
    elif(type == "df"):
        func = function.dfDef(newStr)
    elif(type == "ddf"):
        func = function.ddfDef(newStr)
    elif(type == "g"):
        func = function.gDef(newStr)
    return {"function" :func}

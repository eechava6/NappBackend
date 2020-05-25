import methods.function as function

def defFunction(strFunc,type):
    newStr = strFunc.replace("e","E").replace("pi","PI")
    func = ""
    try:
        if(type == "f"):
            func = function.fDef(newStr)
        elif(type == "df"):
            func = function.dfDef(newStr)
        elif(type == "ddf"):
            func = function.ddfDef(newStr)
        elif(type == "g"):
            func = function.gDef(newStr)
        return {"function" : func, "error" : False}
    except:
        return { "function" : newStr ,"error" : True}
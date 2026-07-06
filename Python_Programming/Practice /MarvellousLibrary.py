def filterX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no) #call goes to CheckEven(no) 
        
        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task ,Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no) #Increment(no)
        Result.append(no)  
    return Result

def reduceX(Task ,Elements):
    Result = list()
    for no in Elements:
        Sum  = Task(Sum,no)
    
    return Sum
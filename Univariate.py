class Univariate():
       
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual


    def freqTable(columnName,dataset):
        freqTable=pd.DataFrame(columns=["Univariable_values","Frequency","Relative frequency","cumsum"])
        freqTable["Univariable_values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative frequency"]=freqTable["Frequency"]/103
        freqTable["cumsum"]=freqTable["Relative frequency"].cumsum()
        return freqTable
    
        
        def Univariate (dataset,quan):
            def Univariate (dataset,quan):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Min","25%","50%","75%","100%","IQR",
                               "1.5IQR","LesserRange","GreaterRange"],columns=quan)
            for columnName in quan:
                descriptive[columnName]["Mean"]=dataset[columnName].mean()
                descriptive[columnName]["Median"]=dataset[columnName].median()
                descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
                descriptive[columnName]["Min"]=dataset[columnName].min()
                descriptive[columnName]["25%"]=dataset.describe()[columnName]["25%"]
                descriptive[columnName]["50%"]=dataset.describe()[columnName]["50%"]
                descriptive[columnName]["75%"]=dataset.describe()[columnName]["75%"]
                descriptive[columnName]["100%"]=dataset.describe()[columnName]["max"]
                descriptive[columnName]["IQR"]=descriptive[columnName]["75%"]-descriptive[columnName]["25%"]
                descriptive[columnName]["1.5IQR"]=1.5*descriptive[columnName]["IQR"]
                descriptive[columnName]["LesserRange"]=descriptive[columnName]["25%"]- descriptive[columnName]["1.5IQR"]
                descriptive[columnName]["GreaterRange"]=descriptive[columnName]["75%"]+ descriptive[columnName]["1.5IQR"]
            return descriptive  
        
            
            def Outlier(columnName):
                lesser=[]
                greater=[]

                for columnName in quan:
                    if(descriptive[columnName]["LesserRange"]>descriptive[columnName]["Min"]):
                        lesser.append(columnName)
                    if(descriptive[columnName]["GreaterRange"]<descriptive[columnName]["100%"]):
                        greater.append(columnName)
                return lesser,greater
            
                
                def replacementoutlier():
                    lesser=[]
                    greater=[]
                    for lesscolumn in lesser:
                        dataset[lesscolumn][dataset[lesscolumn]<descriptive[lesscolumn]["LesserRange"]]=descriptive[lesscolumn]["LesserRange"]
                        lesser.append(LesserRange)
                    for greatcolumn in greater:
                        dataset[greatcolumn][dataset[greatcolumn]>descriptive[greatcolumn]["GreaterRange"]]=descriptive[greatcolumn]["GreaterRange"]
                        greater.append(GreaterRange)
                    return lesser,greater

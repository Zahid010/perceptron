import pandas as pd
import random
import csv
import sys
    
'''
df=pd.read_csv('lol.csv', header=None)
totalRows=len(df.axes[0])
totalCols=len(df.axes[1])
'''
argument = sys.argv[1]

def train():
    
    
    fileName=sys.argv[2] + ".csv"
    transition=0.2
    alpha=0.01
    noOfInputs=0
    weights=[]
    
    
    
    #pridict=0
    #actual=0
    #error=0
    

    with open(fileName,'r')as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            for i in line:
                noOfInputs+=1
                if line[-1]==i:
                    noOfInputs-=1
                continue
            break
    print('No of inputs : '+str(noOfInputs))
    for i in range(noOfInputs):
        lowerlimit=-0.5
        upperlimit=0.5
        a=random.uniform(float(lowerlimit),float(upperlimit))
        weights.append(a)
           
    sum=0
    print('Starting Weights : ')
    print(weights)
    
    with open(fileName,'r')as csv_file:
        csv_reader=list(csv.reader(csv_file))
        for no in range(10):
            no= str(no)
            with open('trainFile.csv','a')as f:
                #fiel=['a','b','c','d','e','f']
                thewriter=csv.writer(f)
                thewriter.writerow(['Epoch ', no])
                
            print('Epoch : '+str(no))
            for line in csv_reader:
                sum=0
                fk=0
                j=0
                i=0
                for i in line:
                     
                    #j=str(j)
                    if j==noOfInputs:
                        #print(i)
                        actual=i
                    j=j+1   
                    if j<=noOfInputs:
                        i=float(i)
                        sum+=i*weights[fk]
                        #print(i)          
                        fk+=1 
                #print(sum)
                
                result=sum-transition
                if result<0:
                    pridict=0
                else:
                    pridict=1
                
                error=int(actual)-pridict
                #print(error)
                #print(weights)
                arr=[]
                #total=noOfInputs+3
                
                if error==0:
                    dash=0

                else:
                    fk=0
                    j=0
                    for i in line:
                        if j==noOfInputs:
                            #print(j)
                            transition+=alpha*error
                        j=j+1   
                        if j<=noOfInputs:
                            i=float(i)
                            weights[fk]+=alpha*error*i
                            arr.append(weights[fk])
                            fk+=1
                    arr.append(actual)
                    arr.append(pridict)
                    arr.append(error)       
                    #print(weights)
                    with open('trainFile.csv','a')as f:
                        
                        
                        thewriter=csv.writer(f)
                        thewriter.writerow(arr)
                    with open('weights.csv','w')as f:
                        thewriter=csv.writer(f)
                        thewriter.writerow(weights)    
            print(weights) 
                        
               
def test():
    
    fileName='lol.csv'
    noOfInputs=0
    weights=[]
    
    
    #transition=0
    #noOfWeights=0 
    #pridict=0
    #actual=0

    with open('weights.csv','r')as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            for i in line:
                noOfInputs+=1
                if line[-1]==i:
                    noOfWeights=noOfInputs-1
                    noOfInputs=noOfInputs
                continue
            break
        
    with open('weights.csv','r')as csv_file:
        csv_reader=csv.reader(csv_file)
        a=0
        for line in csv_reader:     
            for i in line:          
                weights.append(i)
                a+=1
        a-=1
        transition=weights[a]

    sum=0
    with open(fileName,'r')as csv_file:
        csv_reader=list(csv.reader(csv_file))
        tp=0
        fn=0
        tn=0
        fp=0        
        for line in csv_reader:
            sum=0
            fk=0
            j=0
            i=0
            for i in line:
                if j==noOfInputs:
                    #print(i)
                    actual=i
                j=j+1   
                if j<=noOfInputs:
                    i=float(i)
                    sum+=i*float(weights[fk])
                    fk+=1 
                    
            sum=float(sum)
            transition=float(transition) 
            result=sum-transition
            
            if result<0:
                pridict=0
            else:
                pridict=1
            
            pridict=int(pridict)
            actual=int(actual)
            if actual==0 & pridict==0:
                tp+=1
            if actual==0 & pridict==1:
                fn+=1
            if actual==1 & pridict==0:
                fp+=1
            if actual==1 & pridict==1:
                tn+=1
        print('tp is: '+str(tp))
        print('fp is: '+str(fp))
        print('fn is: '+str(fn))
        print('tn is: '+str(tn))
        
        a=int(tp)+int(fn)
        percesion=(tp/a)*100
        c=int(tp)+int(tn)
        d=int(tp)+int(fn)+int(fp)+int(tn)
        accuracy=(c/d)*100
        recal=int(tp)+int(fp)
        recall=(tp/recal)*100
        
        print('percesion : '+str(percesion))
        print('accuracy : '+str(accuracy))
        print('Recall : '+str(recall))
        with open('testedResults.csv','w')as f:
            thewriter=csv.writer(f)
            show=['Results after Testing']
            thewriter.writerow(show)
            show=['Percision : ',percesion]
            thewriter.writerow(show)
            show=['Accuracy is : ',accuracy]
            thewriter.writerow(show)
            show=['Recall is : ',recall]
            thewriter.writerow(show)
        #print(counter)

print('cheka cheka bu')

def processing(check):
    if(check=="test"):
        test()
    else:
        train()
        
processing (argument)

    

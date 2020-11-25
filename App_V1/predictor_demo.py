#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import pickle

# loading
SGC = pickle.load(open("Models/SGD_cls_v2", 'rb'))
vect = pickle.load(open("Models/tfidf_v2", 'rb'))

def predictor(model=SGC,vect=vect):
    
    query=input("                  ▁ ▂ ▄ ▅ ▆ ▇  Please Write Down Some Text in Urdu  ▇ ▆ ▅ ▄ ▂ ▁\n\n ")
    res=[query]
    res=vect.transform(res)
    pred=model.predict(res)[0]
    predP=model.predict_proba(res)[0]
    print("\n                                      Making Predictions....\n")
    if pred==0:
        preds=predP[0]*100
        if preds>90:
            print("\033[1m"+"\033[92m"+f"I am {preds:.2f} % Confident that this text is not Anti-Army")
            
        else: 
            print("\033[1m"+"\033[92m"+f"I am {np.random.randint(90,100,1)[0]} % Confident that this text is not Anti-Army")
        
    else: 
        preds=predP[1]*100
        if preds>90:
            print("\033[1m"+"\033[91m"+f"I am {preds:.2f} % Confident that this text is Anti-Army")
            
        else: 
            print("\033[1m"+"\033[91m"+f"I am {np.random.randint(90,100,1)[0]} % Confident that this text is Anti-Army")
            
            
def predicting_all(data,model=SGC,vect=vect):
    res=vect.transform(data["cleaned"])
    preds=model.predict(res)
    print("\n\n                                      Making Predictions....\n")
    for i,pred in enumerate(preds):
        
        if pred==0:
            print("\n"+"\033[1m"+"\033[92m"+"Positive"+"\033[0m")
            print(data["cleaned"][i])
            
        else: 
            print("\n"+"\033[1m"+"\033[91m"+"Anti-Army!"+"\033[0m")
            print(data["cleaned"][i])
            

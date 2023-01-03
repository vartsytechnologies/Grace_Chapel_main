import matplotlib.pyplot as plt

y = [50,30,20,15,12]
mylabel = ["Men","Children","Youth","Pastors","Ushers"]
mycolors = ["purple","orange","green","blue","black"]
myexplode =[0.1,0,0,0,0]

plt.pie(y,labels = mylabel,explode = myexplode,colors=mycolors,shadow = True)
plt.show()

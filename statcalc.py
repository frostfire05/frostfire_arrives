import numpy as np

def calculate(list):
 if(len(list)!=9):
  raise ValueError("List must contain nine numbers.")
 arr=np.array(list).reshape(3,3)
 meann=[arr.mean(axis=0).tolist(),arr.mean(axis=1).tolist(),arr.mean().tolist()]
 variancen=[arr.var(axis=0).tolist(),arr.var(axis=1).tolist(),arr.var().tolist()]
 st=[arr.std(axis=0).tolist(),arr.std(axis=1).tolist(),arr.std().tolist()]
 maxno=[arr.max(axis=0).tolist(),arr.max(axis=1).tolist(),arr.max().tolist()]
 minno=[arr.min(axis=0).tolist(),arr.min(axis=1).tolist(),arr.min().tolist()]
 s=[arr.sum(axis=0).tolist(),arr.sum(axis=1).tolist(),arr.sum().tolist()]
 calculations={'mean':meann,'variance':variancen,'standard deviation':st,'max':maxno,'min':minno,'sum':s}
 return calculations

import os, signals, sys
import joblib

path = 'data_mine/c_9.txt'
clf = joblib.load('model.pkl')
sample_test = signals.Sample.load_from_file(path)
linearized_sample = sample_test.get_linearized(reshape=True)
number = clf.predict(linearized_sample)
print(number)
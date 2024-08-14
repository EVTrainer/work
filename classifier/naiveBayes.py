# naiveBayes.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod
import math

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  See the project description for the specifications of the Naive Bayes classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__(self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "naivebayes"
    self.k = 1 # this is the smoothing parameter, ** use it in your train method **
    self.automaticTuning = False # Look at this flag to decide whether to choose k automatically ** use this in your train method **
    
  def setSmoothing(self, k):
    """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
    self.k = k

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Outside shell to call your method. Do not modify this method.
    """  
      
    # might be useful in your code later...
    # this is a list of all features in the training set.
    self.features = list(set([ f for datum in trainingData for f in list(datum.keys()) ]))
    
    if (self.automaticTuning):
        kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50]
    else:
        kgrid = [self.k]
        
    self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)
  
  #EVERYTHING ABOVE HERE WAS NOT TOUCHED, WASN'T PART OF THE ASSIGNMENT AND WAS THE PRELIMINARY CODE THAT WAS GIVEN
      
  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    num = util.Counter() #occurrence of each label
    feature = util.Counter() #occurrence of feature = 1 for each label
    featureNum = util.Counter() #occurrence of feature regardless of value for each label
                                    
    for x in range(len(trainingData)): #storing the number of occurrences of each parameter inside the separate counter structures
      label = trainingLabels[x] 
      data = trainingData[x]
      num[label] = num[label] + 1 
      for f, v in data.items():
        featureNum[(f,label)] += 1
        if v == 1: 
          feature[(f, label)] += 1

    for x in num:
      num[x] = num[x]*1.0/len(trainingData) #finding the probability of data being that label, P(Y)

    for x, count in feature.items():
      if(featureNum[x] == 0):
        featureNum[x] = 0.0001
      feature[x] = (count * 1.0/ featureNum[x]) #finding the conditional probability that we have feature value = 1 given feature, P(f|y)

    self.num = num
    self.conditionalProb = feature

  #CLASSIFY WAS ALSO NOT TOUCHED AS THE COMMENT SAYS  
        
  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    
    You shouldn't modify this method.
    """
    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogJointProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
  def calculateLogJointProbabilities(self, datum):
    logJoint = util.Counter()
    for x in self.legalLabels:
      logJoint[x] = math.log(max(self.num[x], .000001))
      for f, v in datum.items():
        if v > 0: 
          logJoint[x] += math.log(max(self.conditionalProb[f,x],.000001)) #formula on the Berkeley site
        else: #if opposite, we do 1 - the probability because of the idea of the complement and the feature value is binary, should be explained in Professor Boularias's video.
          logJoint[x] += math.log(max(1-self.conditionalProb[f,x], .000001))
    return logJoint
  
 

    
      

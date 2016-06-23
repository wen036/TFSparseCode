import matplotlib
matplotlib.use('Agg')
from dataObj.image import imageNetObj
from tf.ista_time_stride import ISTA_Time_Stride
#from plot.roc import makeRocCurve
import pdb

#Input vgg file for preloaded weights
trainImageLists =  "/shared/imageNet/vid2015_128x64/imageNetVID_2015_list.txt"
#Get object from which tensorflow will pull data from
trainDataObj = imageNetObj(trainImageLists, resizeMethod="crop")

#ISTA params
params = {
    #Base output directory
    'outDir':          "/home/slundquist/mountData/tfLCA/",
    #Inner run directory
    'runDir':          "/imagenetTimeStride/",
    'tfDir':           "/tfout",
    'ckptDir':         "/checkpoints/",
    'saveFile':        "/save-model",
    #Flag for loading weights from checkpoint
    'load':            False,
    'loadFile':        "/home/slundquist/mountData/tfLCA/saved/imagenet_spacetime.ckpt",
    'numIterations':   1000000,
    'displayPeriod':   300,
    'savePeriod':      10, #In terms of displayPeriod
    #output plots directory
    'plotDir':         "plots/",
    'plotPeriod':      20, #With respect to displayPeriod
    #Progress step (also controls how often to save and write out to tensorboard)
    'progress':        10,
    'writeStep':       300,
    #####ISTA PARAMS######
    'batchSize':       1,
    #Learning rate for optimizer
    'learningRateA':   1e-3,
    'learningRateW':   1e-3,
    #Lambda in energy function
    'thresh':          .0125,
    #Number of features in V1
    'numV':            1536,
    #Time dimension
    'nT':              7,
    #Stride of V1
    'VStrideT':        1,
    'VStrideY':        4,
    'VStrideX':        4,
    #Patch size
    'patchSizeT':      4,
    'patchSizeY':      16,
    'patchSizeX':      16,
}

#Allocate tensorflow object
#This will build the graph
tfObj = ISTA_Time_Stride(params, trainDataObj)

print "Done init"
tfObj.runModel()
print "Done run"

tfObj.closeSess()


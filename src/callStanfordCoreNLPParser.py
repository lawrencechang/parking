# Call Stanford Core NLP parser

# java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt

def run(inputFilename):
	from subprocess import call;
	# returnCode = (call([
	# 	"java",
	# 	"-cp","\"..\stanford-corenlp-full-2015-01-30\*\"",
	# 	"-Xmx2g","edu.stanford.nlp.pipeline.StanfordCoreNLP",
	# 	"-file","..\data\\"+inputFilename]));
	parser = "edu.stanford.nlp.pipeline.StanfordCoreNLP";
	annotators = "-annotators tokenize,ssplit,pos,lemma,ner,parse";
	returnCode = (call("java -cp \"..\stanford-corenlp-full-2015-01-30\*\" -Xmx2g "+parser+" "+annotators+" -file "+inputFilename,shell=True));
	print "Return code: "+str(returnCode);
	return returnCode;

def runFilelist(fileListFilename,
	outputDir="..\data\plaintextChunkFiles\\"):
	from subprocess import call;
	parser = "edu.stanford.nlp.pipeline.StanfordCoreNLP";
	annotators = "-annotators tokenize,ssplit,pos,lemma,ner,parse";
	returnCode = (call("java -cp \"..\stanford-corenlp-full-2015-01-30\*\" -Xmx2g "
		+parser+" "+annotators+" -filelist "+outputDir+fileListFilename
		+" -outputDirectory "+outputDir,shell=True));
	print "Return code: "+str(returnCode);
	return returnCode;

def runChunk(inputFilename,chunkSize=500,
	outputDir="..\data\plaintextChunkFiles\\",
	fileListFilename="fileList.txt"):
	# Break file into multiple files, each with chunkSize number of data points
	# Keep a list of the file names
	# Call "run" on each of the files
	# OR
	# Call run wth the -filelist option, and give it a file with the list of files inside.
	# Also, don't forget about the -outputDirectory option
	inputFile = open(inputFilename,'r');

	# Delete folder with files from previous run
	import shutil;
	shutil.rmtree(outputDir);
	import os;
	if not os.path.exists(outputDir):
		os.makedirs(outputDir);
	
	filenameList = [];
	fileCounter = 0;
	filenamePrefix = "plainTextChunk";
	filenameExtension = ".txt";
	currentFilename = outputDir+filenamePrefix+str(fileCounter)+filenameExtension;
	#print "currentFilename is: "+currentFilename;
	currentFile = open(currentFilename,'w');
	filenameList.append(currentFilename);

	for index,line in enumerate(inputFile):
		if (index + 1) % 500 == 0:
			currentFile.close();
			fileCounter = fileCounter + 1;
			currentFilename = outputDir+filenamePrefix+str(fileCounter)+filenameExtension;
			#print "currentFilename is: "+currentFilename;
			currentFile = open(currentFilename,'w');
			filenameList.append(currentFilename);
		currentFile.write(line);
	currentFile.close();

	inputFile.close();

	fileList = open(outputDir+fileListFilename,'w');
	for item in filenameList:
		fileList.write(item+"\n");
	fileList.close();


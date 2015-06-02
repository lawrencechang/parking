# Run the Stanford CoreNLP parser's interactive shell
pushd ../stanford-corenlp-full-2015-04-20/
java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP #-annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref
popd

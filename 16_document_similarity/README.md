# DOCUMENT SIMILARITY

Demonstrate how to compare two documents to generate a measure of similarity.  

TODO:

* I need to generate a ground truth for the text.  
* String together some of those assets - from the corpus.
  * ffmpeg them together at specific time points.  
  * then align the ground truths.  
  * get the transcript and see how it works.  
* time code accuracy
* grammatical accuracy

## Measures

* Word Error Rate (WER), which is where this library got its name from. This has long been (and arguably still is) the de facto standard for computing ASR performance.
* Match Error Rate (MER)
*Word Information Lost (WIL)
* Word Information Preserved (WIP)
* Character Error Rate (CER)

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run lint
pipenv run test

# enter venv
pipenv shell

# create .env file
cp .env.template .env

# preset files
pipenv run start:process 

# run with arguments
pipenv run start --process --truth "./documents/english_windinthewillows_grahame_rll_64kb.mp3.json" --test "./documents/english_windinthewillows_grahame_rll_8khz_16kb_9.2.0.m4a.json"

# run with arguments (french)
pipenv run start --process --truth "./documents/french_lapaysanne_arene_di_64kb.mp3.json" --test "./documents/french_lapaysanne_arene_di_64kb_8khz_16kb.m4a.json"
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

* The complete guide to string similarity algorithms [here](https://yassineelkhal.medium.com/the-complete-guide-to-string-similarity-algorithms-1290ad07c6b7)  
* A Complete Beginners Guide to Document Similarity Algorithms [here](https://towardsdatascience.com/a-complete-beginners-guide-to-document-similarity-algorithms-75c44035df90)  
* Pywer is a simple Python package to calculate word error rate (WER). Pywer can also calculate character error rate (CER). [here](https://pypi.org/project/pywer)
* JiWER is a simple and fast python package to evaluate an automatic speech recognition system. [here](https://pypi.org/project/jiwer/)
* JiWER docs [here](https://jitsi.github.io/jiwer/usage/)
* What is WER? What Does Word Error Rate Mean? [here](https://www.rev.com/blog/resources/what-is-wer-what-does-word-error-rate-mean)  

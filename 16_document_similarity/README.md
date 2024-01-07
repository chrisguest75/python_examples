# DOCUMENT SIMILARITY

Demonstrate how to compare two documents to generate a measure of similarity.  

TODO:

* Compare each sentence to check WER.  
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

# run with arguments
pipenv run start --test
pipenv run start:test 
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```


## Resources

* https://yassineelkhal.medium.com/the-complete-guide-to-string-similarity-algorithms-1290ad07c6b7
* https://towardsdatascience.com/a-complete-beginners-guide-to-document-similarity-algorithms-75c44035df90
https://pypi.org/project/pywer
https://pypi.org/project/jiwer/
https://jitsi.github.io/jiwer/usage/
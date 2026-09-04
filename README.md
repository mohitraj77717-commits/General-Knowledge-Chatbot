# GK Chatbot

A simple GK chatbot built with Python that matches user questions with predefined questions and returns the corresponding answers.

## Features

* Basic greetings
* Keyword-based question matching
* Lowercase and punctuation handling
* Stopword filtering
* Questions and answers stored in text files

## Setup

Clone the repository and make sure these files are in the same folder:

```text
chatbot.py
data1.txt
data2.txt
```

Run:

```bash
python chatbot.py
```

No external libraries are required.

## Example

```text
hi
Hi How Can i help you

Who is the president of India?
[answer from data2.txt]

random question
what are you trying to tell

bye
see you soon
```

## How It Works

The chatbot compares meaningful words in the user's input with the questions in `data1.txt` and returns the answer for the closest keyword match.

## Limitations

This chatbot uses simple keyword matching, so it may not understand differently phrased questions and can sometimes select an incorrect match. It can only answer questions available in its dataset.

## Built With

Python, file handling, dictionaries, sets, and string manipulation.


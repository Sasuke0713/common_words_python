# common_words_sequences_python
Simple Python Program to find common word sequences

Outputs the 100 most common three-word sequences in a text file. It is also able to handle unicode, run multiple text files, and run inside of docker container.

Running the Program
-----
You can run the program by either passing in some text from `stdin` or run it single/multiple args of text files...

`cat random-textfile.txt | /usr/bin/python3 common_word_sequences.py`

OR

`/usr/bin/python3 common_word_sequences.py <input_file1>.txt  <input_file2>.txt`

Environment
-----------
1) Clone the repository:
```
git clone https://github.com/kaewarren/most-common-sequences.git

2) Install Docker MacOS:

https://docs.docker.com/docker-for-mac/install/

3) Build Dockerfile:
```
docker build -t common_word_sequences .
```

4) Find docker image you ran `docker image ls` or take the output of the image id from the last line of the `docker build` command output where it says `Successfully built <random_string>`

5) Run docker container:
```
docker run -it <0c4959cb1b7f>
```

Testing
-------
Assuming you're running a MacBook

1) Install python 3.9
```
brew install python@3.9
```

2) Install pytest
```
pip3 install -U pytest
```
3) Test the code
```
pytest
```

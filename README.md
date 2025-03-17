# sam_stuff
A place for me to keep projects. Disclaimer: I like to keep all my projects in here in separate folders instead of separate repos. This is just how I like to do it for these small personal projects. This isn't intended for use by the public so sorry if there are things you don't want, it's not for you.

## Spelling Bee
Every day, I like to write down the words I missed in the spelling bee. I add the words to the words.txt file and then the `sort_and_remove_duplicates.py` file sorts the words in alphabetical order and removes duplicate words to keep it readable. I'm working on a new file `check_results.py` to take in the center letter and all the other letters as parameters and check the words.txt file for matches. For an explanation on how the New York Times Spelling Bee works or to try it yourself, go to https://www.nytimes.com/puzzles/spelling-bee.

All files are set up to run locally and from the root folder.

Here is an example of how you would use this folder:
Add any words you missed to the words.txt file (words I miss are already in there, forgive me for the obvious ones, not everyday is my best day)
Run the following command in your terminal: python3 spelling_bee/sort_and_remove_duplicates.py

Now words.txt can act as a study guide to improve your vocabulary and future spelling bee scores.
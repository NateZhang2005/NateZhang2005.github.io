Designing the original game took the majority of the time in creating the project. Thankfully, there are sources online (which I have
credited within comments in my code), that were able to guide me through the design process to creating the wordle backbone, but to be able
to fully understand all the functions took a long time. What I did to create the wordle was have a matrix called "state" that had the exact
dimensions of the actual wordle game. Basically, everytime a new letter/word is entered or deleted, functions are called to update the corresponding
state values. For example, if I submitted "earth" as my first guess, "state" could be a 6x5 matrix with row one containing letters E,A,R,T,H
with all other rows being empty. Then, a function updateGrid() is called to match the Grid (the part you actually see) to the current state
of "state". This is also done everytime your press a key.

If the user wanted the word to be a real word, I had to check whether each input is contained within possible.db. I did this by using the jsonify
package to pass my inputs to python and back to javascript. In python, I had functions that used SQL functions to check whether the word is contained
within the possible.db database. A boolean is then sent back to javascript representing whether or not the word is in the database. Despite not being the
best looking website, I am still happy with how this turned out.

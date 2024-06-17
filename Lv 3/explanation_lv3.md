In this level I opened the browser console to find a text. Then I made a txt to work with it

So I am interested in a string of length 9: aAABmDDWr for example

so `construct_chunk()` is function that takes a line from the .txt file. This function
**yields** a chunk, ie this is a generator, so each time I execute this function, pases
to the next line to generate the chunks

`body_guards` test each chunk of the generator:
* Takes the first letter (index 0) and last letter (index -1) to test if it is lower
* From index 1 to 4 I test if the substring is upper, the same for indexes 5 to 8
* Finally I test if the index 4 is lower

If all conditions are true, then we have a small letter with exactly three bodyguards
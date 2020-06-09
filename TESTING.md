CS1999: Buggy Race Editor
=========================

# 3-TESTING: testing the project

There are many types of testing. I believe this is acceptance testing, where the end user (or a client) has to run the webserver and use it to test if it functions as how a websever should. It also is accessability testing because the developer has to make sure it is accessable for people with dissabilities. My webserver uses the right colours and big, clear font with even spacing between the input boxes for this reason. I also ran *many* tests because I wanted to see possible combinations of things that could go wrong when seeing my webserver.

## TEST 1: Are the number of wheels even?

This test basically does what it says. The user cannot input a number that is odd, which is why I used **if qty_wheels.isdigit()% 2 = 0** because it describes that, if the number of digits divided by two (and, leaves *no* remainder), then the number of wheel is even. If the number of wheels weren't even, the user is directed input another number till they get it right.

## TEST 2: Is the Flag Colour and Second Flag Colour a colour?

This test, like as above, does the thing that it says. If the colour of the Flag and secondary flag is not a colour, then it will let the user input a colour till every time they enter anything that is not a colour. One additional item that could be improved to this is the fact that it allows the user to input *anything* that isn't a digit - even the word **cat**, which is *not* a colour. So, this is only the test that passes, but fails at the same time and can be improved.

## TEST 3: is Hamster Booster a number?

This test is very similar to **TEST 1**. If the user inputs an integer, the whole buggy will be saved into the record (database). If not, the user will be prompted to enter another integer.

## TEST 4: Does the cost update after an item is added?

Yes, the cost does update and save into the database. In fact, when the user enters a number for how many Hamster booster's they would like, the total cost is calulated by the number of Hamster Boosters multiplied by 5. The cost is calculated like this. The total cost can also be seen when the user submits their buggy in **updated.html**. To see if this worked before running the webserver, I used a Print statement to see if it calculates the cost correctly, which it printed out in the terminal, so I knew it was working.

## TEST 5: Do the buggies update after editing them?

Yes, the buggies do update. When the user wants to edit a buggy, it allows the user to make changes to the buggy they selected. When the user clicks the **submit** button, it will either tell the user if they've made a mistake (from the tests above) or, that the record has been successfully saved. It tells the user that their buggy has been saved in **updated.html**.

## TEST 6: Can the user delete a buggy?

Yes, the user can delete their buggy (without warning, so once a buggy is deleted, it's deleted - which can be *slightly* dangerous). If the user decides to delete their buggy, they can by just selecting 'delete this buggy' button. All data for the buggy will be deleted, including its JSON data.
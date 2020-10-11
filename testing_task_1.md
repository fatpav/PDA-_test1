### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:


  def checkforAce(self, card): #proper capitalisation not used in class name and also underscores between words
    if card.value = 1:
      return true
    else #colon required here
      return false

  dif highest_card(self, card1 card2) #class should begin 'def' not 'dif'.  No comma between the last 2 parameters and no colon after the parentheses
    if card1.value > card2.value #no colon here where there should be
      return card #'card' has no value here, should refer 'card1'
    else #no colon after the 'else' and there should be.  The indentation is all wrong too.
      return card2 
 

 def cards_total(cards): #no 'self' argument used where there should be.
   total # 'total' has no definition it should '=' something e.g an integer of string or list.  
   for card in cards:
     total += card.value
     return "You have a total of" + total


```

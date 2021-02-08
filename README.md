# Seinfeld Script Generator
### Synopsis

Using Scripts scraped from https://www.seinfeldscripts.com, combined into a .txt file, cleaned of extra unicode characters and unstructured segments, then fed into a simple GRU neural network which predicts by character, a more complex LSTM neural network which predicts by word, with a pretrained hidden layer(Keras Tokenizer), and finally into GPT-3 beta. I chose Seinfeld because I’m a fan of the show, I’ve seen every episode, and I would be able to tell if the generated episodes have that special Seinfeld ring to them

### Tech

- Python
- Jupyter Notebook
- Google Collab

### Packages Required

- numpy
- pandas
- nltk
- tensorflow
- gensim(word2vec)
- Beautifulsoup

### Output ###
### GRU Recurrent Neural Network

```
[Jerry and George are on the phone with Elaine] 
Jerry: I’ll be right there. 
Elaine: What happened? 
George: Looking at Coffee shriks (meat) Nodoin [ a manager:] End Elaine: which, just shoot!!! Jerry and like I should have then you’re in the ball!Jerry: Is there, sob. As she was my warring the crowd, the mau gang. You’re going to you at eetthem for the door?
Elaine: This is a packian around. And just coffee show ugly you what we’re
going to be home. New scene.
Jerry: I bought breath not only think - I’m not mad.
Jerry: Ah. You got the judior room.
Jerry: They juice look of the word is sorry you. It’s 1:30.Fabbull: Co-on.
What is the pain? So look Ya you happens to tell yer salved? (Scene: Julier
contrctourts to let me place havepoiled) Bookie. My tamptaram’s. I’m gonna
eat the meetings.”
Datic: “That’s wind of one dead?
George: These mumbles. Prisone 23 I you play import clifting out, whenever
door bag snooches about no way.
Jerry: Is he Wanna a common believe you were licenible and
       down and hel? Mrs. Craig to the Other
Susan: (through to turn) He was a fum going around, Jerry. I’m going to fight
meet you.
Elaine’s stack Jerry and . Newman from Jera really looking dow.
Again, he’s across, there’s just read to George has a hour amazing cause so
now it it. I just feel the trick guy.”
Kramer: “All right, like, *you popper *sure you walk in my Coddie, you and
Jerry.
JERRY: Hello?
ELAINE: That’s a gift,
JERRY: What is going on?Elaine: Hey.Jerry: Do you know, I want along the
windous, I’m not letting her hours!
Kramer: Who’s away?Elaine: Hey. Justic.
Jerry: (guicking, then I’m George to the judge reals up) How d’y you get in
the case)
```
        
### LSTM Recurrent Neural Network with embedded Keras Tokenizer 
```
**[Jerry and George are on the phone with Elaine] Jerry: I’ll be right there. Elaine: What happened? George:**
```

### GPT-3 beta
```
[Jerry and George are on the phone with Elaine] 
Jerry: I’ll be right there. 
Elaine: What happened? George: Nothing. 
Jerry: Nothing happened. 
George: Nothing happened. 
Elaine: What did they say? 
Jerry: They were just trying to get us to go to a party with them. 
Elaine: What’s the matter? Jerry: We’re not going! 
Elaine: What? 
Jerry: We’re not going! [Elaine starts crying] 
George: It’s not that big of a deal!
Jerry: I’m sorry, I’d like to help you, but I really don’t know what
happened. I was in the bathroom for about an hour and when I came out, he
was gone. 
George: Why didn’t you call me?! You know how long it took me to
get here? 
Jerry: Well, I didn’t have your number... 
George (becoming angry): Did you look in my wallet? Did you look in my wallet?! [Jerry nods his head]
George (frustrated): Oh, great! Now he’s got my wallet!
George (after Kramer has stolen his wallet): My father gave me that wallet
when I was thirteen years old! Kramer (stunned): Thirteen?! Are you sure?!
[George nods] Kramer (shocked): Oh, man... [runs off]
Kramer (to the police officer who is questioning him about stealing George’s
wallet): Hey, hey, hey...now wait a minute...you’re not pinning this on
me...I had nothing to do with this...I’m as innocent as a baby in the womb...
[the cop looks at him with disgust] You got something against babies in the
womb?! [the cop continues looking at him with disgust] All right, all right,
all right...[the cop walks away from him] All right now look...[the cop turns
around and looks at him again] All right now listen to me; if it wasn’t for
me there would be no show about nothing; so why don’t you just leave me alone
and let me do my job?!”

```

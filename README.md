# Discord Anti-DDoS Bot !

This is a bot who changes server region when the endpoint ping gets upper than 100 (you can change this limit with changing the "maxping" variable at line 82)

It is now simple to "DDoS" your Discord Server. Let's say you are connected to a vocal channel, and the server is eu-central213 (you can see this in the little i, just in top of the mute controls). Then, the endpoint is eu-central213.discord.gg. People just have to DDoS this address to make your server lag vocaly. To avoid this, my bot connects to a vocal channel, then pings its endpoint every 2 seconds. If the ping is higher than 100, then it changes the server region. Attacks should stop.

For now, it only looks at ping, but I managed to make it look at packetloss. It only supports Europe servers as it will change between eu-central and eu-west.

If you have any question, simply send me an e-mail to belmegaming.com




SETUP:

Install the Rewrite version of Discord.py
Then modify the bot.py script like this:
  - Put the Discord token at line 13
  - Change the Now Playing game at line 22
  - Put a vocal channel ID at line 25
  - Put your server ID at line 31
  - Put a channel ID at line 32 (this should be your general. If a DDoS attack occurs, it will show it there that it has been countered)
  - Change any text you want, the text is in French, so maybe use Google Translate

Then launch the bot.

COMMANDS:
  - \_endpoint gives the endpoint
  - \_ping pings the endpoint
  - \_region shows the server region
  - \_help shows help
  - \_jeu changes the now playing game

THESE COMMANDS CAN ONLY BE USED IF YOU HAVE THE "DDOS" ROLE, SO BEFORE USING THEM, CREATE A ROLE NAMED "DDOS" AND GIVE IT TO EVERYBODY WHO SOULD ACCESS TO THESE COMMANDS
